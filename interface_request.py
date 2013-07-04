# -*- coding: utf-8 -*-
import requests
import hashlib
class InterfaceRequest:
	def __init__(self):
		pass

	def query_user_exchange_log(self, flag, member_name, start_time, end_time):
		md5_key = "abc#%@123"
		a = [end_time, member_name, start_time, md5_key]
		para = '|'
		para = para.join(a)
		para = hashlib.md5(para.encode(encoding="utf-8")).hexdigest()
		print(para);
		url = "http://api.kedou.com/interface/queryUserExchangeLog.htm?flag={0}&memberName={1}&startTime={2}&endTime={3}&sign={4}";
		url = url.format(flag, member_name, start_time, end_time, para);
		r = requests.request("GET", url);
		return r.text;
i = InterfaceRequest();
print(i.query_user_exchange_log("from", "geksong", "13687098","1334569"));