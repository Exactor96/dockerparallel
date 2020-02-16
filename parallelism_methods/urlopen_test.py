from urllib.request import urlopen
from threading import Thread
import time

url = 'http://NBK:8000'
def func():
    urlopen(url=url)

th = [Thread(target=func).start() for i in range(10 ** 9)]

