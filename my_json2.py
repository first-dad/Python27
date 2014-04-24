# -*- coding: utf-8 -*-


from json import load

if __name__ == '__main__':
    x = open('my_json1.json', 'r')
    print load(x)
