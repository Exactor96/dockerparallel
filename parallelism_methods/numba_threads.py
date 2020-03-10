from ctypes import c_void_p
from threading import Thread
from numba import jit, void, int_, char
from ctypes import pythonapi


def thread_exec(func, nums_thread, signature, list_args):
    numba_func = jit(signature, nopython=True)(func)

    threads = [Thread(target=numba_func, args=chunk)
               for chunk in list_args]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

savethread = pythonapi.PyEval_SaveThread
savethread.argtypes = []
savethread.restype = c_void_p

restorethread = pythonapi.PyEval_RestoreThread
restorethread.argtypes = [c_void_p]
restorethread.restype = None

def make_3_dim_list(count):
    threadstate = savethread()
    lst = []
    # start = time.monotonic()
    for i in range(count):
        for j in range(count):
            for g in range(count):
                lst.append([i, j, g])
    restorethread(threadstate)


if __name__ == '__main__':
    import time
    start = time.monotonic()
    thread_exec(make_3_dim_list, 8, void(int_), [[100,], [100,], [100,], [100,], [100,], [100,], [100,], [100,],])
    print(time.monotonic() - start)