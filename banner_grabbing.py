#!/usr/bin/env python
import socket
import sys

if len(sys.argv) <= 2:
    print('USE: {} 10.0.0.1 80'.format(sys.argv[0]))
else:
    ip = sys.argv[1]
    port = int(sys.argv[2])

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((ip, port))
    banner = my_socket.recv(1024)

    print(banner)
