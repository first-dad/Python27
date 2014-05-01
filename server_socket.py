# -*- coding: utf-8 -*-


import socket


if __name__ == '__main__':
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(('localhost ', 8000))

    while True:
        srv.listen(100)
        sock, address = srv.accept()
        (host, port) = address

        while True:
            message = sock.recv(1024)

            if not message:
                break

            words_num = message.lower().count('python')

            log = open('python.log', 'a')
            log.write('%s:%s найдено %d слов "python"\n' % (host, port, words_num))
            log.close()

            print u'Received from %s:%s: %s' % (host, port, message.decode('utf-8'))

            sock.send(u'кол-во слов "python" в вашей строке - %s'.encode('utf-8') % words_num)

        sock.close()
