import cloudpickle
import socket
sock = socket.socket()

sock.bind(('',1442))
#sock.listen(1)

#conn, addr = sock.accept()

while True:
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(4096*10)
    if not data:
        break
    s = cloudpickle
    Dict = s.loads(data)
    e = Dict()

    conn.sendall(s.dumps(e))
conn.close()