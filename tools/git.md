# Git

1. [git status 显示中文和解决中文乱码](https://blog.csdn.net/u012145252/article/details/81775362)

    ```shell
    # 方法一
    git config --global core.quotepath false
    # 方法二
    vi ~/.gitconfig
    [core]
        quotepath = false
    ```

2. git 忽略目录，但不忽略其下某个文件
    .gitignore如下配置，达到忽略node_modules目录，但不忽略其下fileSaver的效果。

    ```shell
    /node_modules/*
    !/node_modules/fileSaver
    ```

3. 推送时报错

    ```shell
    warning: ----------------- SECURITY WARNING ----------------
    warning: | TLS certificate verification has been disabled! |
    warning: ---------------------------------------------------
    warning: HTTPS connections may not be secure. See https://aka.ms/gcmcore-tlsverify for more information.
    ```

    检查发现，因为之前使用其他代码仓库时，因其证书问题，暂时不做验证（`git config http.sslVerify`为false），只要将其改成true即可:`git config --global http.sslVerify true`。

4. 仓库迁移

    ```shell
    git clone --bare https://gitlab.xxxxx.com/abc/ccccc.git
    cd ccccc.git
    git push --mirror http://e.devops.xxxxx.com/abc/ccccc.git
    ```

5. difftool

    [git difftool 使用 p4merge，DiffMerge 或者 Beyond Compare 4_MICROAU的博客-CSDN博客](https://blog.csdn.net/zhufu86/article/details/118930307)

6. log

    ```shell
    # 不分页、无交互
    git --no-pager log
    ```

## 在线资料

[git-diff忽略^M.](https://blog.csdn.net/asdfgh0077/article/details/104157910)
[git的fast forward &amp; git命令学习 &amp; no-ff - blcblc - 博客园](https://www.cnblogs.com/charlesblc/p/6132384.html)
[git merge 的两种模式的区别  --no-ff与fast forward_rd_w_csdn的博客-CSDN博客_git merge 模式](https://blog.csdn.net/rd_w_csdn/article/details/114871924)