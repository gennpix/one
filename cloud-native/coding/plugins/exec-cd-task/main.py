# coding:utf8
# 半成品

import argparse
import json

try:
    # 优先使用环境里已经装有的
    import requests
except ImportError:
    # 运行环境里没有, 使用 qciplugin 里的 requests
    import qciplugin._vendor.requests as requests

OPENAPI_URL = "https://maxoio.coding.net/open-api"
headers = {"Authorization": "token xxxxxx"}
# OPENAPI_URL = "http://codingcorp.can.anchnet.com/open-api"
# headers = {"Authorization": "token xxxxxx"}


class TPPluginError(RuntimeError):
    pass


def get_apps():
    data = {"Action": "DescribeCdApplications"}
    data = json.dumps(data)
    resp = requests.post(OPENAPI_URL, data, headers=headers)
    print(resp.status_code)
    print(json.dumps(resp.json(), indent=4))


def get_app():
    data = {"Action": "DescribeCdApplication", "Application": "jettest"}
    data = json.dumps(data)
    resp = requests.post(OPENAPI_URL, data, headers=headers)
    print(resp.status_code)
    print(json.dumps(resp.json(), indent=4))


def create_cd_task():
    task_json = {
        "job": [
            {
                "type": "CreateCdTask",
                "application": {
                    "cloudProviders": "kubernetes,hostserver",
                    "email": "gennpix@163.com",
                    "nickName": "maxoio",
                    "instancePort": 80,
                    "name": "test",
                },
                "user": "maxoio",
            }
        ],
        "application": "test",
        "description": "Create Application: test",
    }
    data = {"Action": "CreateCdTask", "TaskJsonContent": json.dumps(task_json)}
    data = json.dumps(data)
    resp = requests.post(OPENAPI_URL, data, headers=headers)
    if resp.status_code != 200:
        raise TPPluginError("[ERROR] 执行CD任务状态码[{}]不等于200".format(resp.status_code))

    print(json.dumps(resp.json(), indent=4))
    return resp.json()


def trigger_cd_pipeline():
    task_json = {
        "user": "maxoio",
        # "param": None,
        "artifacts": [
            {
                # "artifactAccount": "generic::12550975",
                # "customKind": False,
                # "id": "68459f87-552a-4a6a-82af-b2bba27e07f0",
                "name": "maxoio-generic.pkg.coding.net/devops-demo/generic/blj.sh",
                "parentType": "generic",
                "pkgId": 3770182,
                "pkgName": "blj.sh",
                "projectId": 9334829,
                "projectName": "devops-demo",
                "repoName": "generic",
                "type": "coding_artifact/generic",
                "uriName": "devops-demo",
                # "needFilter": False,
                "version": "latest",
                # "reference": "maxoio-generic.pkg.coding.net/devops-demo/generic/blj.sh:latest",
            }
        ],
    }
    data = {
        "Action": "TriggerCdPipeline",
        "Application": "test",
        "PipelineNameOrId": "test",
        "TriggerJsonContent": json.dumps(task_json),
    }
    data = json.dumps(data)
    resp = requests.post(OPENAPI_URL, data, headers=headers)
    if resp.status_code != 200:
        raise TPPluginError("[ERROR] 执行CD任务状态码[{}]不等于200".format(resp.status_code))

    print(json.dumps(resp.json(), indent=4))
    return resp.json()


def main(args):
    get_apps()
    # trigger_cd_pipeline()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="调用CD流水线.")
    parser.add_argument("--xxx", metavar="xxx", help="xxx")
    main(parser.parse_args())
