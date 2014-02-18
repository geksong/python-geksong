# -*- coding: utf-8 -*-
import socket, traceback

host = ""
port = 51423

ser = socket.socket(socket.AF_INET, socket.SOCK_DRAM)
ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ser.bind((host, port))

while 1:
    try:
        message, address = ser.recvfrom(8192)
        print "Got data from ", address
        ser.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
