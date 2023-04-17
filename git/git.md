# git

## 文档

https://git-scm.com/book/en/v2

Submodules：https://git-scm.com/book/en/v2/Git-Tools-Submodules

## 常用

1. 两个commit之间的差异文件：`git diff ${GIT_PREVIOUS_COMMIT} ${GIT_COMMIT} --name-only`
2. `git config --global merge.commit no &&  git config --global merge.ff no`
3. 最近一次提交: `git rev-parse --short HEAD` 或者 `git rev-parse HEAD`
