import os
import sys

sys.path.append(os.path.abspath('../../'))

import socket
from core.serializer import serializer
from core.executor import Executor as executor


sock = socket.socket()

sock.bind(('', 1442))
#sock.listen(1)

#conn, addr = sock.accept()
import time
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    data = conn.recv(4096 * 10)
    if not data:
        break
    s = serializer()
    Dict = s.deserialize(data)
    e = executor(**Dict)
    ts = time.monotonic()
    e.run()
    print(time.monotonic() - ts)
    conn.sendall(s.serialize(e.result))
conn.close()
