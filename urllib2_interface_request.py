# -*- coding: utf-8 -*-
import hashlib
import urllib2
import urllib
import json

class Interface_request:
	def __init__(self):
		pass

	def query_user_exchange_log(self, flag, member_name, start_time, end_time):
		md5_key = "abc#%@123"
		a = [end_time, member_name, start_time, md5_key]
		para = '|'
		para = para.join(a)
		para = hashlib.md5(para.encode(encoding="utf-8")).hexdigest()
		req = urllib2.Request('http://api.kedou.com/interface/queryUserExchangeLog.htm')
		qs = {'flag':flag,'memberName':member_name,'startTime':start_time,'endTime':end_time,'sign':para}
		qs = urllib.urlencode(qs)
		req.add_data(qs)
		opener = urllib2.build_opener()
		rest = opener.open(req)
		return rest.read()

if __name__ == '__main__':
	irq = Interface_request()
	res = irq.query_user_exchange_log("from", "geksong", "13687098","1334569")
	print res
	o_res = json.loads(res)
	print o_res['result']
	print o_res['mesCode']