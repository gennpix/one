# MarkDown

## 编辑器

编写用vscode，阅读用typora。

1. vscode插件(Markdown All in One,Markdown Preview Enhanced,Markdown PDF,markdownlint)
2. [typora](https://www.typora.io/)

## 注释

```markdown
# 单行注释
[comment]: <> (This is a comment, it will not be included)
[comment]: <> (in  the output file unless you use it in)
[comment]: <> (a reference style link.)
[//]: <> (This is also a comment.)
[//]: # (This may be the most platform independent comment)

# 多行注释
Blank line 空行
[^^]:
    commentted-out contents
    should be shift to right by four spaces
Blank line 空行
```

> [comments-in-markdown](https://stackoverflow.com/questions/4823468/comments-in-markdown)

## 链接

```markdown
# 行内式链接
[内容](https://rmbrx.com)
→ <a href="https://rmbrx.com">内容</a>

[内容](https://rmbrx.com "title")
→ <a href="https://rmbrx.com" title="title">内容</a>

# 参考式链接
Blank line 空行
[参考链接]: https://rmbrx.com "title"

[内容1][参考链接]
→ <a href="https://rmbrx.com" title="title">内容1</a>

[内容2][参考链接]
→ <a href="https://rmbrx.com" title="title">内容2</a>

# 锚点(页面内跳转，与HTML锚点一样的效果，无论几级标题)
[内容](#标题文字)
→ <a href="#标题文字">内容</a>
[内容](#指定标题文字 "title")
→ <a href="#标题文字" title="title">内容</a>

# md文件间跳转
#  1. 跳转到当前目录下的abc.md
[内容](abc.md)
#  2. 跳转到上级目录下的aaa.md
[内容](../aaa.md)
#  3. 跳转到当前目录下的abc.md，并指定位置（锚点）
[内容](abc.md#指定标题文字)
```

## 表格

```markdown
| 标题1 | 标题2 |  标题3 |
| :-- | :--: | --: |
| 左对齐 | 居中对齐 | 右对齐 |
| 表格内换行<br>第2行 | 表格内换行<br>第2行 | 表格内换行<br>第2行 |
```

效果展示：
| 标题1 | 标题2 |  标题3 |
| :-- | :--: | --: |
| 左对齐 | 居中对齐 | 右对齐 |
| 表格内换行<br>第2行 | 表格内换行<br>第2行 | 表格内换行<br>第2行 |
