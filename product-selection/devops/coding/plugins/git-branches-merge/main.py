# coding:utf8
import argparse

from common import TPPluginError
from git import (
    get_all_branches,
    checkout_env_branch,
    get_merged_branches,
    filter_merged_branches,
    merge_branches,
    merge_branch,
    push_code,
    generate_branches_list,
    set_ssh_private_key,
    git_clone_code,
    check_branch_exist,
    set_git_config,
)


def check_params(args):
    dest_branch = args.dest_branch
    if not dest_branch:
        raise TPPluginError("[ERROR] 目标分支参数不能为空")
    branches = args.branches
    if not branches:
        raise TPPluginError("[ERROR] 分支列表参数不能为空")
    subsystem = args.subsystem
    if not subsystem:
        raise TPPluginError("[ERROR] 子系统参数不能为空")

    return dest_branch, branches.split(","), subsystem


def main(args):
    dest_branch, branch_list, subsystem = check_params(args)
    pre_merge_branch = args.pre_merge_branch.strip() if args.pre_merge_branch else ""
    set_ssh_private_key()
    set_git_config()
    git_clone_code()
    all_branches = get_all_branches()
    checkout_env_branch(dest_branch, all_branches)  # checkout到 目标分支
    if pre_merge_branch and pre_merge_branch!="不使用":  # 检查预合并分支是否存在
        check_branch_exist(pre_merge_branch, all_branches["remote"])
        merge_branch(pre_merge_branch, dest_branch)  # 如果设置了预合并分支，则执行预合并操作

    for branch in branch_list:  # 检查分支列表中的分支是否都存在
        check_branch_exist(branch, all_branches["remote"])

    merged_branches = get_merged_branches(branch_list)
    merged_branches, new_branches = filter_merged_branches(merged_branches, dest_branch)

    if merge_branches(dest_branch, branch_list, merged_branches, new_branches):
        push_code(dest_branch)  # 合并代码

    merged_branches = get_merged_branches(branch_list)
    merged_branches, _ = filter_merged_branches(merged_branches, dest_branch)
    generate_branches_list(subsystem, dest_branch, merged_branches)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="根据输入的分支列表，自动合并到指定目标分支.")
    parser.add_argument("--subsystem", metavar="subsystem", help="子系统名称", required=True)
    parser.add_argument(
        "--dest_branch", metavar="dest_branch", help="目标分支", required=True
    )
    parser.add_argument(
        "--branches", metavar="branches", help="分支列表，逗号分隔", required=True
    )
    parser.add_argument(
        "--pre_merge_branch", metavar="pre_merge_branch", help="预合并分支/管理分支"
    )

    main(parser.parse_args())
