# git

## 文档

https://git-scm.com/book/en/v2

Submodules：https://git-scm.com/book/en/v2/Git-Tools-Submodules

## 常用

1. 两个commit之间的差异文件：`git diff ${GIT_PREVIOUS_COMMIT} ${GIT_COMMIT} --name-only`
2. `git config --global merge.commit no &&  git config --global merge.ff no`
3. 最近一次提交: `git rev-parse --short HEAD` 或者 `git rev-parse HEAD`
4. 清空密码: `git config --global --unnset ccredential.helper`
5. 清除用户配置: `git config --global --unnset user.name`  `git config --global --unnset user.email`

## 问题

1. root 用户下 git clone 失败，提示 Repository NOT FOUND，但其他用户下正常。
   检查git 配置 `git config -l`，如果有user.name/user.email/credential.helper 等配置，可能是其用户没权限，请reset该配置

   ```shell
    git config --global --unset user.name
    git config --global --unset user.email
    git config --global --unset credential.helper
   ```
