# 自定义网站

> https://docs.github.com/cn/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#choosing-a-publishing-source

1. 创建仓库
1. 创建一个index.html文件，内容随意
1. settings --> 找到 GitHub Pages块 --> 选择分支、目录，点击save保存
1. 创建一个CNAME文件，内容为你需要设置的域名，比如`maxoio.com`
1. 以阿里云为例，配置域名解析
    ```
    主机记录  记录类型 解析线路 记录值 TTL 状态  备注
    @	CNAME	默认 gennpix.github.io  10 分钟	正常
    ```
   > https://docs.github.com/cn/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site
1. 等待一会儿，settings --> 找到 GitHub Pages块 --> 选中 Enforce HTTPS，这样最终用户将通过 https://maxoio.com 访问我的blog
   > https://docs.github.com/cn/github/working-with-github-pages/securing-your-github-pages-site-with-https
1. 访问测试： 可以正常访问。发现证书已经从R3（Let's Encrypt）自动申请好了，时长为3个月（这个证书怎么更新？待验证是否github自动更新！）
1. 因为国内访问github网速较慢，流量不大的话，可以白嫖一个cdn，暂时未搞定。。。
1. 添加404页面
   > https://docs.github.com/cn/github/working-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site
1. todo: 要使用gh-pages分支

# vuepress

1. md仓库
1. ci
   > https://blog.csdn.net/qq_21567385/article/details/106935923
   > https://www.cnblogs.com/MuYunyun/p/6082359.html
   > https://github.com/baidu/amis/blob/master/.github/workflows/gh-pages.yml
   > https://github.com/OrangeSAM/Blog/blob/master/deploy.sh
1. cdn、图床
1. 全球加速
