# -*- coding: utf-8 -*-


class Log(object):
    """
    Класс логирования

    Декораты по-желанию можно
    прикрутить к методам стека push и pop,
    чтобы отслеживать вызов
    """
    @staticmethod
    def push(method):
        def wrapper(__self, value):
            print 'pushing...'
            method(__self, value)

        return wrapper

    @staticmethod
    def pop(method):
        def wrapper(__self):
            print 'popping...'
            method(__self)

        return wrapper


class Stack(object):
    def __init__(self, size):
        self.__size = size
        self.__index = 0
        self.__item = []

    @Log.push
    def push(self, value):
        if self.is_full():
            raise Exception('Невозможно добавить значение в полный стек')
        else:
            self.__item.insert(self.__index, value)
            self.__index += 1

    @Log.pop
    def pop(self):
        if self.is_empty():
            raise Exception('Невозможно получить значение из пустого стека')
        else:
            self.__index -= 1
            item = self.__item[self.__index]
            del self.__item[self.__index]
            return item

    def is_empty(self):
        return self.__index == 0

    def is_full(self):
        return self.__index == self.__size

    def __str__(self):
        return str(self.__item)


if __name__ == '__main__':
    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print stack
    stack.pop()
    stack.pop()
    print stack
    stack.push(2)
    stack.push(3)
    print stack
    stack.pop()
    stack.pop()
    stack.pop()
    print stack
    stack.push(2)
    stack.pop()
    print stack

