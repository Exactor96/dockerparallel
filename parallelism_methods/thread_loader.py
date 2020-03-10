from threading import Thread
from wget import download
from numba import jit, void, int_, char#, string
from ctypes import pythonapi, c_void_p
from urllib.request import urlretrieve
from types import FunctionType

savethread = pythonapi.PyEval_SaveThread
savethread.argtypes = []
savethread.restype = c_void_p

restorethread = pythonapi.PyEval_RestoreThread
restorethread.argtypes = [c_void_p]
restorethread.restype = None


def download_file(url):
    threadstate = savethread()
    urlretrieve(url, url.split('/')[-1])
    restorethread(threadstate)


def multithread_download(url_list):
    numba_func = jit(nopython=True)(download_file)

    threads = [Thread(target=numba_func, args=url_i)
               for url_i in url_list]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    url_list = [
        [f'http://s12.seplay.net/content/stream/films/altered.carbon.s02e01.720p.rus.lostfilm.tv_172489/hls/720/segment{i}.ts',]
        for i in range(1, 100, 1)
    ]
    print(url_list)
    multithread_download(url_list)
