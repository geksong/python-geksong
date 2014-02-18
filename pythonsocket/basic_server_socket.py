# -*- coding: utf-8 -*-
'''
简单的服务器实现
'''
import socket, traceback

host = ""
port = 51423

# step 1: Create the server socket
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# step 2: Set the socket options
ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# step 3: Bind to a port and interface
ser.bind((host, port))
# step 4: Linsten for connections
ser.listen(1)
print "Watting for connection"

# wait for connections
while 1:
    try:
        clientsock, clientaddr = ser.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    try:
        print "Got connection from " , clientsock.getpeername()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
