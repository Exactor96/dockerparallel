import socket
from serializer.serializer import serializer

def deco(func):
    def wrap(*args,**kwargs):
        sock = socket.socket()
        sock.connect(('dietpi', 1441))
        s = serializer()
        snd={'func': func, 'globals': globals(), "locals": locals()}
        snd.get('locals').update({'sock': None})
        sock.sendall(s.serialize(snd))
        data = sock.recv(4096)
        #sock.close()

        print(s.deserialize(data))
    return wrap


@deco
def srt(l):
    return sorted(l)

@deco
def colazz(num):
    res = []
    if num == 1:
        return [1,]
    while num != 1:
        if num % 2 == 0:
            res.append(num)
            num /= 2
        elif num % 2 == 1:
            res.append(num)
            num = num * 3 + 1
    return res


import sqlite3
@deco
def db_test():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('create table T (int t)')
    return cur.lastrowid
@deco
def gen(n):
    for i in range(n):
        yield i

import requests
@deco
def send_req(url):
    r = requests.get(url)

    return r.content

if __name__ == '__main__':
    # l = [-96, -19, 64, -43, 81, -65, -77, -53, 57, -53, -65, 86, 77, 98, 99, -52, 42, -61, 93, -8, -84, -80, -68, 90,
    #      -10, -91, -69, 80, -73, -50, 70, -54, -68, 23, -84, -50, 75, -15, 15, 97, 33, 89, -60, 53, 47, 70, 96, 2, -64,
    #      -16, -25, 54, -12, -59, -84, -77, -67, 91, 92, 67, 45, 64, 100, 62, -32, 20, -26, -91, -45, 39, 100, 16, -60,
    #      -13, -49, 63, -46, -84, 71, -76, -70, -79, 85, 28, -81, -35, -75, -73, 77, -70, 23, -87, -67, 100, 17, -24, 62,
    #      2, 37, 70]
    # srt(l)
    # import random
    #
    # for i in range(10**6):
    #     srt([random.randint(-10**6,10**6) for j in range(random.randint(10,100))])

    #Collazz
    #for i in range(1,111):
    #    colazz(i)
    #db_test()
    #gen(10)
    send_req('http://ident.me/')