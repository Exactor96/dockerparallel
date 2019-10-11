import socket
from serializer.serializer import serializer
from executor.executor import executor


sock = socket.socket()

sock.bind(('',1441))
sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    s = serializer()
    Dict = s.deserialize(data)
    e = executor(**Dict)
    e.run()

    conn.send(s.serialize(e.result))

conn.close()