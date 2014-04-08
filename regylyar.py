# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text') as f:
        print 'With"with":'
        print f.read()

    print

    f = open('text')
    print 'Without"with":'
    print f.read()
