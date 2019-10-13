import cloudpickle
import sqlite3

def db_test():
    con  = sqlite3.connect('test.db')
    cur = con.cursor()
    res = cur.execute('create table T (int t);')
    return res


import socket

sock = socket.socket()
sock.connect(('localhost', 1442))
s = cloudpickle
snd = db_test
sock.sendall(s.dumps(snd))
data = None
while True:
    data += sock.recv(4096)
# sock.close()

print(s.loads(data))

print(cloudpickle.loads(data))