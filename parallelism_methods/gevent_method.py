import time
import gevent
from gevent import monkey
monkey.patch_all()
from funcs_for_test import make_3_dim_list
from urllib.request import urlopen
import random


def make_3_dim_list(count, add=''):
    lst = []
    start = time.monotonic()
    for i in range(count):
        for j in range(count):
            for g in range(count):
                lst.append([i, j, g])
    print(time.monotonic() - start, add, count)


jobs = [gevent.spawn(make_3_dim_list, n * random.randint(1, 100)) for n in range(8)]
gevent.joinall(jobs)
