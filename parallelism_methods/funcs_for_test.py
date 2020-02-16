import time


def make_3_dim_list(count, add=''):
    lst = []
    start = time.monotonic()
    for i in range(count):
        for j in range(count):
            for g in range(count):
                lst.append([i, j, g])
    print(time.monotonic() - start, add)


def last_number_of_factorial(x):
    f = 1
    start = time.monotonic()
    for i in range(1, x + 1):
      f *= i
    print(time.monotonic() - start, f % 10)
