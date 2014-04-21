# -*- encoding: utf-8 -*-
#!/usr/bin/env python
import interf_test
'''
File: finance_interf.py
Author: geksong
Description: 挖财金融接口测试
'''
def test_finduser(siteId, userId, key):
    '''
    Author: geksong
    Description: 查询用户
    '''
    para = dict(siteId=siteId, userId=userId)
    url = "http://localhost:8080/finance/hx/interf/finduser.action"
    res = interf_test.test_finance_interf(url, para, key)
    return res

def test_updateposition(siteId, userId, key):
    '''
    Author: geksong
    Description: 更新华夏基金持仓
    '''
    para = dict(siteId=siteId, userId=userId)
    url = "http://localhost:8080/finance/hx/interf/updateposition.action"
    res = interf_test.test_finance_interf(url, para, key)
    return res

if __name__ == '__main__':
    key = "123$%678%456"
    siteId = "huaxia"
    userId = "1776535"
    print test_updateposition(siteId, userId, key)
