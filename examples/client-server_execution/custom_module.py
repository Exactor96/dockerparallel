import os


import requests


def send(url):
    return requests.get(url).content

class T:
    def __init__(self,a):
        self.a = a

    def run(self):
        print(self.a)

