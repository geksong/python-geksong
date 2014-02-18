# -*- coding: utf-8 -*-

import socket
import sys

port = 80
host = sys.argv[1]
filename = sys.argv[2]
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((host, port))
soc.sendall(filename + "\r\n")
while 1:
    rec = soc.recv(2048)
    if not len(rec):
        break
    sys.stdout.write(rec)
soc.close()