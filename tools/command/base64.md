# base64

Linux下用base64命令加解密字符串

加密：
$ echo Hello World | base64
SGVsbG8gV29ybGQK

解密：

$ echo SGVsbG8gV29ybGQK | base64 -d
Hello World