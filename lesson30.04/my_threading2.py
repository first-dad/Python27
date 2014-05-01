# -*- coding: utf-8 -*-

__author__ = 'Илья'

from threading import Thread
from Queue import Queue
import time
import random


class T(Thread):
    def __init__(self, q):
        super(T, self).__init__()
        self.q = q
        self.setDaemon(True)


class T1(T):
    def run(self):
        while True:
            print self.q.get()


class T2(T):
    def run(self):
        while True:
            time.sleep(1)
            self.q.put(random.randint(1, 100))

if __name__ == '__main__':
    q = Queue()
    t1 = T1(q)
    t2 = T2(q)

    t1.start()
    t2.start()

    time.sleep(5)