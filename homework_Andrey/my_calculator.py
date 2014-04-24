# -*- coding: utf-8 -*-


__author__ = 'Илья'


class Num(object):
    value1 = float(raw_input("Введите первую переменную: "))
    value2 = float(raw_input("Введите вторую переменную: "))


class Func(Num):
    operator = raw_input("Введите действие: ")

    def __init__(self):
        self.result = 0

    def action(self):
        if self.operator == '+':
            self.result = Num.value1 + Num.value2
        elif self.operator == '-':
            self.result = Num.value1 - Num.value2
        elif self.operator == '*':
            self.result = Num.value1 * Num.value2
        elif self.operator == '/':
            self.result = Num.value1 / Num.value2
        print "{0} {1} {2} = {3}" .format(Num.value1, self.operator, Num.value2, self.result)


def calculator():
    n = Func()
    n.action()
    cal = raw_input("Выключить калькулятор? (да/нет): ")
    if cal == "да":
        print "Приятного полёта"
    else:
        print "Подскажите как заново запустить калькулятор..."

if __name__ == '__main__':
    calculator()