import random
from numba import jit
import numba
# Serial version
@jit(nopython=True)
def monte_carlo_pi_serial(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

# Parallel version
@jit(nopython=True, parallel=True)
def monte_carlo_pi_parallel(nsamples):
    acc = 0
    # Only change is here
    for i in numba.prange(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

import time
start = time.monotonic()
monte_carlo_pi_serial(int(4e8))
print(time.monotonic() - start)
start = time.monotonic()
monte_carlo_pi_parallel(int(4e8))
print(time.monotonic() - start)