from funcs_for_test import make_3_dim_list
from concurrent.futures import ProcessPoolExecutor as PPE
from memory_profiler import memory_usage
mem = memory_usage(-1, interval=.2, timeout=1)
n = 200
t = 8

ppe = PPE(max_workers=8)


r = ppe.map(make_3_dim_list,[n,] * t)
next(r)
print(mem)