# -*- coding: utf-8 -*-


import re


if __name__ == '__main__':
    print re.compile(r'[0-9]+').findall('6546 dht 584sdrt')
    print re.compile(r'Hello(?!=World)').findall('HelloWorld HelloDaddy')
    print re.compile(r'Hello(?=World)').findall('HelloWorld HelloDaddy 684gr hguyggkb')
    print re.compile(r'o{1,3}').findall('HelloWorld HelloDaddy 654gvr rtvee5')
    print re.compile(r'[^ll]').findall('HelloWorld HelloDaddy rger45 r45gt')
    print re.compile(r'(Hello | o)').findall('Hello World HelloDaddy 354arge rg354')
    print re.compile(r'(Hello)?(?(1) (World) | (Hell))').findall('Hello World HelloDaddy Hell argt43 254ref')
    print re.compile(r'(Hell)?\d+\1\1').findall('Hello World HelloDaddy Hell654HellHell argt43 254ref')
    print re.compile(r'\d{2}.\d{2}.\d{4}').findall(' 02.03.1236 20.03.1456 Hello World HelloDaddy Hell654HellHell argt43 254ref')