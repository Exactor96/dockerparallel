from funcs_for_test import make_3_dim_list
from threading import Thread
from memory_profiler import memory_usage
mem = memory_usage(-1, interval=.2, timeout=1)
n = 200
t = 8

threads = [Thread(target=make_3_dim_list, args=[n, i]) for i in range(t)]
for th in threads:
    th.start()
    th.join()
print(mem)