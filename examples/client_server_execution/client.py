import socket
from serializer.serializer import serializer
from examples.client_server_execution.custom_module import T

def deco(func):
    def wrap(*args,**kwargs):
        sock = socket.socket()
        sock.connect(('dietpi', 1442))
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
@deco
def work_with_custom_module(Class):
    c = Class('123')
    c.run()


t = T('asd')
work_with_custom_module(T)

