# -*- coding: utf-8 -*-


import socket
import random


def generate_string(word):
    string = ''

    for _ in range(1, random.randrange(3, 10)):
        string += word + ' '

    return string

if __name__ == '__main__':
    python_string = generate_string('python')

    port = 8000

    print 'Отправляем строку: %s' % python_string
    print

    for address in ['192.168.0.1%.2d' % num for num in range(1, 20)]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((address, port))
            sock.send(python_string.encode('utf-8'))

            print
            print '-----------------------------------'
            print 'Установлено соединение с сервером: %s:%s' % (address, port)
            print 'Ответ: %s' % sock.recv(1024)
            print '-----------------------------------'
            print
        except:
            print "Can't connect to %s:%s" % (address, port)

        sock.close()