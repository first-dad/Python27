# -*- coding: utf-8 -*-

__author__ = 'Илья'

from threading import Thread, Lock
import time, threading


lock = Lock()

def method():
    lock.acquire()
    time.sleep(5)
    print "HI from Thread {}". format(threading.current_thread().name)
    lock.release()


class T(Thread):
    def run(self):
        print u'я запустился... {}'. format(threading.current_thread().name)
if __name__ == '__main__':
    th = Thread(target=method, name='th1', args=())
    #th.setDaemon(True)   сделать поток независимым от родителя
    th.start()
    th.join()

    th2 = Thread(target=method, name='th2', args=())
    th2.start()

    th3 = T(name='th3')
    th3.start()