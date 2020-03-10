import os
import sys

sys.path.append(os.path.abspath('../../'))

import socket
from core.serializer import serializer


def deco(func):
    def wrap(*args, **kwargs):
        sock = socket.socket()
        sock.connect(('localhost', 1442))
        s = serializer()
        snd = {'func': func, 'globals': globals(), "locals": locals()}
        snd.get('locals').update({'sock': None})
        sock.sendall(s.serialize(snd))
        data = sock.recv(4096)
        #sock.close()

        return s.deserialize(data)
    return wrap


@deco
def srt(l):
    return sorted(l)

@deco
def colatz(num):
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
def count_response_size(url):
    r = requests.get(url)
    return r.content.__sizeof__()


@deco
def work_with_custom_module(Class):
    c = Class('123')
    c.run()


if __name__ == '__main__':
    # Sorting
    import time
    from random import randint
    print('Unsorted List')
    unsorted_list = [randint(-10 ** 9, 10 ** 9) for i in range(15)]
    print(unsorted_list)
    print('Sorted List')
    print(srt(unsorted_list))
    print('\n'*3)
    time.sleep(3)
    # collatz function
    print('Collatz Function for 1337')
    print('is', colatz(1337))
    time.sleep(3)
    print('\n' * 3)
    print('Count response size')
    print('ya.ru', count_response_size('http://ya.ru/'), 'bytes')
    print('google.com', count_response_size('http://google.com/'), 'bytes')
    print('vk.com', count_response_size('http://vk.com/'), 'bytes')
    print('facebook.com', count_response_size('http://facebook.com/'), 'bytes')
