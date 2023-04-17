# Gitea

## 创建自定义模板目录

`mkdir -p /data/gitea/templates/custom`

## 创建自定义html目录

`mkdir -p /data/gitea/public`

## 使用自定义的公共文件(自定义gitea)

https://docs.gitea.io/zh-cn/customizing-gitea/#%E4%BD%BF%E7%94%A8%E8%87%AA%E5%AE%9A%E4%B9%89%E7%9A%84%E5%85%AC%E5%85%B1%E6%96%87%E4%BB%B6

## 创建自定义html
`wget -O /data/gitea/public/privacy.html https://raw.githubusercontent.com/go-gitea/gitea/master/contrib/legal/privacy.html.sample`

## 增加额外的footer

`vi /data/gitea/templates/custom/extra_links_footer.tmpl`
内容如下:
`<a class="item" href="{{AppSubUrl}}/privacy.html">Privacy Policy</a>`