import socket
from serializer.serializer import serializer
from executor.executor import executor


sock = socket.socket()

sock.bind(('',1442))
#sock.listen(1)

#conn, addr = sock.accept()

while True:
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(4096)
    if not data:
        break
    s = serializer()
    Dict = s.deserialize(data)
    e = executor(**Dict)
    e.run()

    conn.sendall(s.serialize(e.result))
conn.close()