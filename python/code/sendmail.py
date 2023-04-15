#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'user@xx.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USER_TLS = True
MAIL_USE_SSL = True
EMAIL_TIMEOUT = 10

sender = EMAIL_HOST_USER
receivers = ['receiver@xx.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("测试From", 'utf-8')
message['To'] = Header("测试to", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

smtpObj = smtplib.SMTP(EMAIL_HOST)
smtpObj.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.close()