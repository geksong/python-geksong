# -*- encoding: utf-8 -*-
#!/usr/bin/env python
import type_check
import types
import time
import urllib2
import urllib
'''
File: interf_test.py
Author: geksong
Description: test http interface
'''
def digest_sign(paraDict, key):
	'''
	Author: geksong
	Description: caculate sign
	'''
	join_char = "||"
	if isinstance(paraDict, dict):
		paraDict.update(time=int(time.time()))
		paraList = sorted(paraDict.items(), key=lambda d:d[0].lower(), reverse=False)
		uncodesign = ""
		for k,v in paraList:
			uncodesign += str(v) + join_char
		uncodesign += key
		sign = type_check.digest_as_md5(uncodesign)
		paraDict.update(sign=sign)
		return paraDict
	return None

def test_finance_finduser(siteId, key, userId):
	'''
	Author: geksong
	Description: test connect to finance finduser interface
	'''
	find_user_url = "http://localhost:8080/finance/hx/interf/finduser.action"
	para = dict(siteId=siteId, userId=userId)
	paraDic = digest_sign(para, key)
	if paraDic is None:
		print "Error: para is null[%s]" % paraDic
	else:
		urlpara = urllib.urlencode(paraDic)
		finduser = None
		try:
			finduser = urllib2.urlopen(find_user_url, urlpara)
		except urllib2.URLError,e:
			print e
		if finduser is None:
			print "Error: finduser error"
		else:
			res = finduser.read()
			return res
	return ""

if __name__ == '__main__':
	key = "123$%678%456"
	para_dict = {"siteId":"huaxia", "userId":"8100626"}
	print digest_sign(para_dict, key)
	print test_finance_finduser("huaxia", key, "8100625")
