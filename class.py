# -*- coding: utf-8 -*-

"""class Utka:
    def kryakat(self):
        print "Kryakat", self
    def __str__(self):
        return "Utka"
u= Utka()
u.kryakat()"""

#"""a+b   тоже   a.__add__(b) """

# issubclass(b,a)
# ._x    инкапсуляция
"""
class Auto:
    maxSpeed = 130
    model = 'LADA'
    def drive(self,time):
        print self.model, "проехал" , float(time)/60/60*self.maxSpeed * self.Benzine.kpd, "км"
    def __init__(self, model, effectivnost):
        self.model = model
        self.effectivnost = effectivnost
    def test(self, speed):
        print "Скорость"
class Benzine:
    def __init__(self, tip, kol, kpd):
        self.tip = tip
        self.kol = kol
        self.kpd = kpd



car = Auto()
car.drive(10)
"""


'''
class Auto:
    max_speed = 130
    model = 'Lada'
    km1100 = 7.5
    vback = 40
    toplivo = None
    def km(self,time):
        print (self.max_speed*time)/3600
    def zalitToplivo(self,fuel,vol):
        self.vback = vol
        self.toplivo = fuel
    def testdrive(self,km):
        print km/(self.max_speed*self.toplivo.kpd)
class Toplivo:
    kpd = 1.0
class Benz95(Toplivo):
    kpd = 0.95
car = Auto()
benz = Benz95
car.zalitToplivo(benz,100)
car.testdrive(100)
'''


#class Benzakolonka:
#    bk =
 #   print 'Еду по {}'. format('асфальту')



'''
class Auto1(object):

   # def__init__(self):
    #    print "__init__",self

   # def__new__(cls):
    #    print "__new__",cls
     #   super (Auto1,cls).__new__(cls)
    @staticmethod
    def gabarity():
        return (3.8,1.7)

class Auto:
    max_speed = 130
    model = 'Lada'
    km1100 = 7.5
    vback = 40
    toplivo = None

    @staticmethod
    def gabarity():
        return (3.5,1.5)
    def km(self,time):
        print (self.max_speed*time)/3600
    def zalitToplivo(self,fuel,vol):
        self.vback = vol
        self.toplivo = fuel
    def testdrive(self,km):
        print km/(self.max_speed*self.toplivo.kpd)

print "Габариты лады :" , Auto.gabarity()

class Toplivo:
    kpd = 1.0
class Benz95(Toplivo):
    kpd = 0.95
'''


'''
import time


class Date(object):

    def __init__(self,val):
        self.value = val

    @classmethod
    def now (cls):
        t = time.localtime()
        return cls(t)

    def __str__(self):
        return 'fuck'


class EuroDate(Date):
    def __str__(self):
        return "%d-%d-%d" % (self.value.tm_year,
                             self.value.tm_mon,
                             self.value.tm_mday)

val = time.localtime()
d = Date(val)
d2 = d.now()
print d
print d2
ed = EuroDate(val)
ed2 = EuroDate.now()
print ed
print ed2
'''


'''
l = Lada()
l.model = "BMW"
print l.modul
'''


'''
car = Auto()
benz = Benz95
car.zalitToplivo(benz,100)
car.testdrive(100)
'''



'''
class A(object):
    def setx(self,x):
        self._x = x
    def getx(self): return self._x
    def delx(self): del self._x


a = A()
a.x = 7
'''



'''
class Auto(object):
    _col = None
    cost = 300000
    def setcol(self,col):
        self._col = col
        self.cost -= 10000
    def getcol(self):
        return self._col
    def delcol(self):
        del self._col
    color = property(getcol,setcol,delcol,"I'm color")

a = Auto()
a.color = "green"
a.color = "red"
a.color = "blue"
print help(Auto.color)
print  "color:", a.color, "cost:", a.cost
'''

'''
реализовать на класах модель карты
52 карты по значимости 4 масти
действия "добрать руку","сходить"
козырь
'''


'''
class A:
    @staticmethod
    def a():
        pass

a = A()
a.b()
A.a()
'''


'''
@classmethod
def create(cls):
    return cls()
b = B.create()   # Если класс В наследуется от класса А
'''


'''
class C(object):
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        self.__x = x**2

    @x.deleter
    def x(self):
        del self.__x


c = C()
c.x = 7
print c.x
'''


'''
def__new__(cls,*args,**kwargs):
    pass
'''


'''
import weakref
                                   # слабая ссылка
class Service(object):
    def setCar(self,car):
        self.car = weakref.ref(car)
'''


'''
class A(object):
    __slots__ = ('name')
    name = 7
a = A()
print a.name
'''


'''class Foo:
    __metaclass__ = ABCMeta
    @abstractmethod
    def method(self): pass         # абстрактный класс
    @abstractproperty
    def name(self): pass
'''


'''__metaclass__ = type
class Foo(Meted):                 # метакласс
    pass
'''


'''
class_name = 'A'
class_body = 'pass'
class_dict = {}
class_parents = (object,)
exec(class_body, globals(), class_dict)

A = type(class_name,class_parents,class_dict)

#class A(object):
#    pass
a = A()
print type(A)
'''


'''
class DocMeta(type):
    def __init__(self,name,bases,dict):
        for key, value in dict.items():
            if key.startswith('__'):
                continue
            if not hasattr(value,'__call__'): continue
            if not getattr(value,'__doc__'):
                raise TypeError('%s must have docstring' % key)
        type.__init__(self, name, bases, dict)

class Documented:
    __metaclass__ = DocMeta

class Foo(Documented):
    def spam(self):
        "it's a good method.."
        print "spam"
'''


'''
добавить метод свойств, статический метод, использовать метод класса, использовать метакласс
'''


'''
@dekor
def func():
    pass                        #декоратор

def dekor(func):
    def newFunc():
        print "dekorfunc",func
        func()
    return newFunc
'''

from datetime import datetime
@time
def func():
    print datetime.now()
