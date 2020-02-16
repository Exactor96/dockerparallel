from funcs_for_test import make_3_dim_list
from multiprocessing import Process
from memory_profiler import memory_usage
mem = memory_usage(-1, interval=.2, timeout=1)
n = 200
p = 8

processes = [Process(target=make_3_dim_list, args=(n, i)) for i in range(p)]
for proc in processes:
    proc.start()

print(mem)