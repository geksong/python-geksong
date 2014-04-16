# -*- encoding: utf-8 -*-
#!/usr/bin/env python
import types
import hashlib
'''
File: type_check.py
Author: geksong
Description: check data type
'''
def check_string(data):
	''' check data is a string'''
	if isinstance(data, types.StringType):
		return True
	return False

def digest_as_md5(data):
	'''
	Author: geksong
	Description: digest string as md5
	'''
	if check_string(data):
		m = hashlib.md5()
		m.update(data)
		return m.hexdigest()
	return ""
	
if __name__ == '__main__':
	res = digest_as_md5("123456")
	print res
