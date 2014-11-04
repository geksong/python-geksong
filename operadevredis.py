# -*- coding: utf-8 -*-
import redis
import hashlib

redis_cl = redis.Redis(host='192.168.1.246', port=6380)
redis_info = redis_cl.info()
for key in redis_info:
    print "%s:%s" % (key, redis_info[key])


print "dbSize: %s" % (redis_cl.dbsize())

md5_util = hashlib.md5()
md5_util.update('P2P_YET_VIR_B_AMOUNT')
r_key = md5_util.hexdigest()
print r_key
print "P2P_YET_VIR_B_AMOUNT: %s" % (redis_cl.hget(r_key, 'v1'))
