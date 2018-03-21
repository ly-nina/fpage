#coding:utf-8

import socket
import sys

HOST = '182.254.209.84'
PORT = '9999'

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST,int(PORT)))
print('Connect success.')
c.send(b'TPGPS,123456789ABCDEF,XB01,119.216223,26.034026,201801012000,50,27,END')
data = c.recv(1024)
print(data)
c.close()
