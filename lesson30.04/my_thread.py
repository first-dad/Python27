# -*- coding: utf-8 -*-

__author__ = 'Илья'

from threading import Thread, Lock
#import time, threading


lock = Lock()


def method():
    lock.acquire()
   # time.sleep(5)
    text = "Привет Мир\n"
    f = open("my.txt", "a")
    f.write(text)
    lock.release()


def method2():
    lock.acquire()
   # time.sleep(5)
    text = "Это Вася\n"
    f = open("my.txt", "a")
    f.write(text)
    lock.release()


def method3():
    lock.acquire()
   # time.sleep(5)
    text = "Всем пока\n"
    f = open("my.txt", "a")
    f.write(text)
    lock.release()


if __name__ == '__main__':
    th = Thread(target=method, args=())
    #th.setDaemon(True)   сделать поток независимым от родителя
    th.start()
    th.join()

    th2 = Thread(target=method2, args=())
    th2.start()
    th2.join()

    th3 = Thread(target=method3, args=())
    th3.start()
    th3.join()