# -*- encoding: utf-8 -*-
import httplib, urllib

uids = "1776535,138976"
params = urllib.urlencode({"uids":uids})

headers = {"Content-type":"application/x-www-form-urlencoded",
           "Accept":"text/plain"}

conn = httplib.HTTPConnection("127.0.0.1", port=8080)
conn.request("POST", "/finance/interf/event/sendwanlicaibao.action", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()
print data
