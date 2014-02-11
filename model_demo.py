# -*- coding: utf-8 -*-
from urllib2_interface_request import Interface_request
irq = Interface_request()
res = irq.query_user_exchange_log("from", "geksong", "13687098","1334569")
print res
#o_res = json.loads(res)
#print o_res['result']
#print o_res['mesCode']