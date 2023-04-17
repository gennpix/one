# coding:utf8
import os
import datetime
import json
import shutil

from collections import OrderedDict

from common import TPPluginError
from common import exec_cmd


def set_ssh_private_key():
    private_key_path = os.environ.get("SSH_PRIVATE_KEY_PATH", "")
    if not private_key_path:
        raise TPPluginError("[ERROR] 请定义一个用于部署的私钥凭据，环境变量名称为SSH_PRIVATE_KEY_PATH")
    if not os.path.exists(private_key_path):
        raise TPPluginError("[ERROR] 私钥凭据文件 SSH_PRIVATE_KEY_PATH 不存在")
    cmd = "ln -s {} ~/.ssh/id_rsa".format(private_key_path)
    # 安全考虑，执行但不打印结果
    exec_cmd(cmd)


def git_clone_code():
    git_repo_url = os.environ.get("GIT_REPO_URL", "")
    if not git_repo_url:
        raise TPPluginError("[ERROR] 请选择一个代码仓库！")

    # 如下两个要求是bug，解决后就可以放开检查了
    # 1. 要求工作目录为空
    # 2. 要求在插件子步骤前增加一个shell子步骤，用于改变工作目录
    workdir = os.environ.get("WORKSPACE")
    if not os.path.exists(workdir) or os.path.abspath(os.curdir) != workdir:
        raise TPPluginError("[ERROR] 工作目录错误，请在插件子步骤前增加一个shell子步骤。")

    if os.listdir(workdir):
        raise TPPluginError("[ERROR] 工作目录不为空，会导致克隆代码失败。")

    print("正在克隆代码仓库:{}".format(git_repo_url))
    cmd = "git clone {} {}".format(git_repo_url, workdir)
    return_code, outs = exec_cmd(cmd)
    print(outs)
    if return_code != 0:
        raise TPPluginError("[ERROR] 克隆代码仓库失败!")


def get_all_branches():
    print("获取分支所有分支:")
    cmd = "git branch -a"
    return_code, outs = exec_cmd(cmd)
    if return_code != 0:
        raise TPPluginError("[ERROR] 获取所有分支失败!")

    branches = {"local": [], "remote": []}
    for branch in outs.split("\n"):
        branch = branch.strip()
        # 忽略的记录
        if not branch or branch.startswith("remotes/origin/HEAD -> "):
            continue
        # 远程分支
        if branch.startswith("remotes/origin/"):
            branches["remote"].append(branch[15:])
            continue
        # 本地分支
        if branch.startswith("* "):
            branches["local"].append(branch[2:])
        else:
            branches["local"].append(branch)

    print("  本地分支 {}".format(list(branches["local"])))
    print("  远程分支 {}".format(list(branches["remote"])))
    return branches


def set_git_config():
    cmd = "git config --global merge.commit no &&  git config --global merge.ff no"
    exec_cmd(cmd, error_raise=True)


def remote_branch_name(branch_name):
    return "remotes/origin/{}".format(branch_name)


def local_branch_name(branch):
    return branch[15:]


def check_branch_exist(branch_name, remote_branches):
    if branch_name in remote_branches:
        return True

    raise TPPluginError("[ERROR] 分支[{}]不存在".format(branch_name))


def checkout_env_branch(branch_name, branches):
    print("\n切换分支 {}:".format(branch_name))
    if branch_name in branches["remote"]:
        cmd = "git checkout {} && git pull origin {}".format(branch_name, branch_name)
    else:
        cmd = "git checkout -b {}".format(branch_name)

    return_code, outs = exec_cmd(cmd)
    print(outs)
    if return_code != 0:
        raise TPPluginError("[ERROR] 切换分支:{}失败!".format(branch_name))


def merge_branch(src_branch, dest_branch):
    cmd = 'git merge {} -m "自动合并分支 {} 到 {}"'.format(
        remote_branch_name(src_branch), src_branch, dest_branch
    )
    print(cmd)
    return_code, outs = exec_cmd(cmd)
    print(outs)
    if return_code != 0:
        print("[ERROR] 合并分支 {} 到 {} 失败".format(src_branch, dest_branch))
        cmd = "git status && git diff"
        return_code, outs = exec_cmd(cmd)
        raise TPPluginError(outs)


def merge_branches(dest_branch, feature_branches, merged_branches, new_branches):
    merged = False
    for branch in feature_branches:
        if branch in merged_branches:
            print("分支 {} 已经合入 {} ，无需重复合并。".format(branch, dest_branch))
            continue

        if branch in new_branches:
            print("分支 {} 是新建分支，未进行过开发，无需合并。".format(branch))
            continue

        print("\n正在将分支 {} 合并到 {} ".format(branch, dest_branch))
        merged = True
        merge_branch(branch, dest_branch)

    return merged


def push_code(branch):
    print("\n推送代码到远程分支 {}".format(branch))
    cmd = "git push origin {}".format(branch)
    print(cmd)
    return_code, outs = exec_cmd(cmd)
    print(outs)
    if return_code != 0:
        raise TPPluginError("[ERROR] 推送代码到远程分支 {} 失败, 返回值:{}".format(branch, outs))


def get_merged_branches(branch_list):
    cmd = "git branch -a --merged"
    return_code, outs = exec_cmd(cmd)
    if return_code != 0:
        raise TPPluginError("[ERROR] 获取当前分支在本迭代的需求清单失败")

    branches = [
        local_branch_name(branch.strip())
        for branch in outs.split("\n")
        if branch.strip().startswith("remotes")
        and local_branch_name(branch.strip()) in branch_list
    ]
    return branches


def git_diff_files(src_branch, dest_branch):
    cmd = "git diff {} {} --name-only".format(
        src_branch, remote_branch_name(dest_branch)
    )
    return_code, outs = exec_cmd(cmd)
    if return_code != 0:
        raise TPPluginError("[ERROR] 获取文件差异失败，命令：{}".format(cmd))

    return outs


def generate_branches_list(subsystem, dest_branch, merged_branches):
    print("\n正在生成合并分支清单.")
    # timestamp = datetime.datetime.today().strftime("%Y%m%d")
    short_commit_id = get_last_commit_id(short_flag=True)
    data = OrderedDict()
    data["subsystem"] = subsystem
    data["repo"], repo_name = get_repo_name()
    data["branch"] = dest_branch
    data["commit_id"] = short_commit_id
    data["merged-branches"] = sorted(merged_branches)
    diff_files = [l for l in git_diff_files("master", dest_branch).split("\n") if l]
    data["changed-files"] = diff_files

    filename = "{}.tplist.json".format(short_commit_id)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    list_filename = "{}.tplist.csv".format(short_commit_id)
    with open(list_filename, "w") as f:
        for b in merged_branches:
            diff_list = [
                "{},{}".format(b, l)
                for l in sorted(git_diff_files("master", b).split("\n"))
                if l
            ]
            f.write("\n".join(diff_list))
            f.write("\n")

    shutil.copyfile(filename, "tplist.json")


def get_merge_base(branch1, branch2):
    cmd = "git merge-base {} {}".format(branch1, branch2)
    return_code, outs = exec_cmd(cmd)
    if return_code != 0:
        raise TPPluginError("[ERROR] 执行 {} 失败".format(cmd))

    return outs


def filter_merged_branches(merged_branches, dest_branch):
    merged_branches_result = []
    new_branches = []  # 新的分支，即还没有新增任何代码的分支，需要排除掉
    for branch in merged_branches:
        first_commit = get_merge_base(dest_branch, remote_branch_name(branch))
        second_commit = get_merge_base("master", remote_branch_name(branch))
        if first_commit != second_commit:
            merged_branches_result.append(branch)
        else:
            new_branches.append(branch)

    return merged_branches_result, new_branches


def get_last_commit_id(short_flag):
    if short_flag:
        cmd = "git rev-parse --short HEAD"
    else:
        cmd = "git rev-parse HEAD"
    return_code, outs = exec_cmd(cmd)
    if return_code != 0:
        raise TPPluginError("[ERROR] 执行 {} 失败".format(cmd))

    return outs.strip()


def get_repo_name():
    cmd = "git remote -v| head -1 | awk '{print $2}'"
    return_code, outs = exec_cmd(cmd)
    if return_code != 0:
        raise TPPluginError("[ERROR] 获取仓库名称失败，命令: {}".format(cmd))

    return outs.strip(), outs.split("/")[-1].strip()[:-4]
