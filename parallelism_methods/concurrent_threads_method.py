from funcs_for_test import make_3_dim_list
from concurrent.futures import ThreadPoolExecutor as TPE
from memory_profiler import memory_usage
mem = memory_usage(-1, interval=.2, timeout=1)
n = 200
t = 8

tpe = TPE(max_workers=4)


r = tpe.map(make_3_dim_list,[n,] * t)
next(r)
print(mem)