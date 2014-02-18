# -*- coding: utf-8 -*-
'''
File: update_host.py
Author: geksong
Description: host文件操作
'''
import traceback

def annotate_all(file_path):
    """注释掉所有的host设置，切换到外网"""
    host_file = open(file_path, "w+")
    all_lin = []
    try:
        while True:
            lin = host_file.readline()
            if not len(lin):
                break
            all_lin = all_lin + "#" + lin
            print all_lin
        print all_lin
        host_file.write(all_lin)
        host_file.flush()
    except:
        traceback.print_exc()
    finally:
        host_file.close()

if __name__ == '__main__':
    host_path = "c:/Windows/System32/drivers/etc/hosts"
    annotate_all(host_path)
