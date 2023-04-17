# coding:utf8
# 用法：python main.py --host http://domain --keyword project --headers '{...}'

import argparse
import copy
import json

from config import custom_roles
from default import default_host, default_headers
from roles import permissions, request_body_struct

try:
    # 优先使用环境里已经装有的
    import requests
except ImportError:
    # 运行环境里没有, 使用 qciplugin 里的 requests
    import qciplugin._vendor.requests as requests


class TPPluginError(RuntimeError):
    pass


def get_projects(host, keyword, page, headers):
    url = "{}/api/user/projects/v2".format(host)
    print("url:{}".format(url))
    body = {
        "page": page,
        "pageSize": 30,
        "type": "all",
        "sortBy": {"value": "DESC", "key": "CREATE"},
    }
    if keyword:
        body["keyword"] = str(keyword)

    body = json.dumps(body)
    resp = requests.post(url, body, headers=headers)
    if resp.status_code != 200:
        raise TPPluginError("[ERROR] 获取项目列表状态码[{}]不等于200".format(resp.status_code))
    if resp.json().get("code", "") != 0:
        raise TPPluginError(
            "[ERROR] 获取项目列表接口返回code[{}]不等于0".format(resp.json().get("code", ""))
        )

    return (
        resp.json()["data"]["list"],
        not resp.json()["data"]["page"] == resp.json()["data"]["totalPage"],
    )


def get_roles(host, project, headers):
    url = "{}/api/platform/permission/project/{}/roles".format(host, project)
    print("url:{}".format(url))
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise TPPluginError("[ERROR] 项目角色列表状态码[{}]不等于200".format(resp.status_code))
    if resp.json().get("code", "") != 0:
        raise TPPluginError(
            "[ERROR] 获取项目列表接口返回code[{}]不等于0".format(resp.json().get("code", ""))
        )
    # print(json.dumps(roles, indent=4, ensure_ascii=False))
    return resp.json()["data"]


def delete_default_roles(host, project, roles, headers):
    roles_to_delete = ["开发", "测试", "项目经理", "产品", "运维"]
    for role in roles:
        if role["name"] not in roles_to_delete:
            continue

        url = "{}/api/platform/permission/project/{}/role/{}".format(
            host, project, role["roleId"]
        )
        resp = requests.delete(url, headers=headers)
        if resp.status_code != 200:
            raise TPPluginError(
                "[ERROR] 删除默认角色【{}】状态码[{}]不等于200".format(role["name"], resp.status_code)
            )

        if resp.json().get("code", "") == 0:
            print("[INFO] 成功删除默认角色【{}】".format(role["name"]))


def create_roles(host, project, roles, headers):
    for role in custom_roles:
        if role in roles:
            continue
        url = "{}/api/platform/permission/project/{}/role".format(host, project)
        params = {"name": role, "description": ""}
        resp = requests.post(url, params=params, headers=headers)
        if resp.status_code != 200:
            raise TPPluginError(
                "[ERROR] 创建角色【{}】状态码[{}]不等于200".format(role, resp.status_code)
            )

        if resp.json().get("code", "") == 0:
            print("[INFO] 成功创建角色【{}】".format(role))


def asign_perms(host, project, roles, headers):
    roles_id_map = {r["name"]: r["roleId"] for r in roles}
    for role in custom_roles:
        body = copy.deepcopy(request_body_struct)
        perms = []  # 权限名称，格式为"类别/权限项"
        for m, ps in custom_roles[role].items():
            for p in ps:
                perms.append("{}/{}".format(m, p))

        all_perms = [permissions[p] for p in perms]  # 从权限配置中获取具体的权限值
        coding_perms = copy.deepcopy(permissions["basic"])
        for ps in all_perms:
            for p in ps:
                if p not in coding_perms:
                    coding_perms.append(p)

        body["permissions"] = coding_perms
        url = "{}/api/platform/permission/project/{}/roles/{}/permissions".format(
            host, project, roles_id_map[role]
        )
        body = json.dumps(body)
        resp = requests.put(url, body, headers=headers)
        if resp.status_code != 200:
            raise TPPluginError("[ERROR] 更新角色【{}】权限状态码[{}]不等于200".format(role, resp.status_code))

        if resp.json().get("code", "") != 0:
            print(resp.json())
            raise TPPluginError("[ERROR] 更新角色【{}】权限失败".format(role))

        print("[INFO] 成功更新角色【{}】权限".format(role))


def main(args):
    print("输入参数:\n  keyword:[{}]\n  host:[{}]\n  headers:[{}]"
          "".format(args.keyword, args.host, args.headers))
    keyword = args.keyword

    host = args.host if args.host else default_host

    if args.headers:
        headers = json.loads(args.headers)
    else:
        headers = default_headers

    print(
        "执行参数:\n  keyword:[{}]\n  host:[{}]\n  headers:[{}]".format(
            keyword, host, headers
        )
    )

    if not host.startswith("http"):
        raise TPPluginError("[ERROR] host 参数错误!")

    page = 1
    all_projects = []
    while True:
        projects, has_next = get_projects(host, keyword, page, headers)
        if projects:
            all_projects.extend(projects)
            page += 1
        else:
            break

        if not has_next:
            break

    # print(json.dumps(all_projects, indent=4, ensure_ascii=False))
    for project in all_projects:
        roles = get_roles(host, project["id"], headers)
        delete_default_roles(host, project["id"], roles, headers)
        roles = get_roles(host, project["id"], headers)
        create_roles(host, project["id"], [r["name"] for r in roles], headers)
        roles = get_roles(host, project["id"], headers)
        asign_perms(host, project["id"], roles, headers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="为项目创建自定义权限的用户组.")
    parser.add_argument("--host", metavar="host", help="coding host，http开头")
    parser.add_argument("--keyword", metavar="keyword", help="项目名称")
    parser.add_argument("--headers", metavar="headers", help="请求头")
    main(parser.parse_args())
