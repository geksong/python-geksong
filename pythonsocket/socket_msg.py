# -*- coding: utf-8 -*-

import socket
import sys

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done"
port = 80
so.connect(("www.baidu.com", port))
print "Connected from ", so.getsockname()
print "Connect to ", so.getpeername()
try:
    so.sendall("GET %s HTTP/1.0\r\n\r\n" % "/")
except socket.error, e:
    print "Error msg: %s" % e
    sys.exit(1)
try:
    so.shutdown(1)
except socket.error, e:
    print "Error (detected by shutdown ): %s" % e
    sys.exit(1)

while 1:
    try:
        buf = so.recv(2048)
    except socket.error, e:
        print "Error recive: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    print buf
