import socket

from serializer.serializer import serializer


def deco(func):
    def wrap(*args,**kwargs):
        sock = socket.socket()
        sock.connect(('localhost', 1441))
        s = serializer()
        snd={'func': func, 'globals': globals(), "locals": locals()}
        snd.get('locals').update({'sock': None})
        sock.sendall(s.serialize(snd))
        data = sock.recv(4096)
        #sock.close()

        print(s.deserialize(data))
    return wrap


