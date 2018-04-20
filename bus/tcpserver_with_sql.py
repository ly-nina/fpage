#coding:utf-8
import socket
import threading
import time
import sqlite3
import config
ID = ['123456789ABCDEF']
NAME = ['XB01']
DB_PATH = './db/bus.db'

def tcplink(sock, addr):
    while True:
        data = sock.recv(1024)
        data_decode = data.decode('utf-8')
        if not data or data_decode == 'exit':
            break
        print(data)
        
        msg = data_decode.split(',')
        if msg[0]!='TPGPS' or msg[-1]!='END':
            sock.send(b'GPS01')
        elif msg[1] not in config.ID:
            sock.send(b'GPS02')
        elif msg[2] not in config.NAME:
            print(msg[2])
            sock.send(b'GPS03')
        elif len(str(msg[3]))>12:
            print(msg[3])
            sock.send(b'GPS04')
        elif len(str(msg[4]))>11:
            sock.send(b'GPS05')
        elif len(str(msg[5]))!=12:
            sock.send(b'GPS06')
        elif len(str(msg[6]))>2 or len(str(msg[7]))>2:
            sock.send(b'GPS07')
        else:
            sock.send(b'GPSOK')
            latlng = '%s,%s' %(msg[3], msg[4])
            conn = sqlite3.connect(config.DB_PATH)
            c = conn.cursor()
            print('ok')
            c.execute('insert into gps(name, latlng, temperature, humidity)\
		 values("%s","%s", %d, %d)' % (msg[2], latlng, int(msg[6]),int(msg[7])))
            conn.commit()

    sock.close()
    print('conn from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))
s.listen(5)
print('waiting for conn')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock,addr))
    t.start()
