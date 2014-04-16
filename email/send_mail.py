# -*- encoding: utf-8 -*-
#!/usr/bin/env python
import os
'''
File: send_mail.py
Author: geksong
Description: 发送邮件
'''
def send_mail(mail_address, content):
	"""
	向指定地址发送邮件内容
	"""
	os.path("F:/hello/dkksklj/ldk.jsp")
	print "已向%s发送邮件，内容%s" % (mail_address, content)
if __name__ == '__main__':
	send_mail("zengzhangsong@gmail.com", "哈哈哈哈，python测试邮件")
