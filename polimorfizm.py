# -*- coding: utf-8 -*-
"""def get_last(x):
    return [-1]
print get_last([1,2,3])"""


"""def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data: break
        data = converter(data)
        writer.write(data)"""



class utka:
    def __init__(self,name):
        self.name = name
u = utka('Alex')
print (u)
class gus(utka):
    def __init__(self,name):
        self.peria = 'green'
        super(gus,self),__init__(name)
