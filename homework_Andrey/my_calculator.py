# -*- coding: utf-8 -*-


__author__ = 'Илья'
import fractions


class Calculator(object):
    def __init__(self, value1, value2, operator):
        self.value1 = value1
        self.value2 = value2
        self.operator = operator

    def action(self):
        if self.operator == '+':
            self.result = self.value1 + self.value2
        elif self.operator == '-':
            self.result = self.value1 - self.value2
        elif self.operator == '*':
            self.result = self.value1 * self.value2
        elif self.operator == '/':
            self.result = self.value1 / self.value2
        print "{0} {1} {2} = {3}" .format(self.value1, self.operator, self.value2, self.result)


if __name__ == '__main__':
    while 1:
        calc = Calculator(
            float(raw_input("Введите первую переменную: ")),
            float(raw_input("Введите вторую переменную: ")),
            raw_input("Введите действие: ")
        )
        calc.action()
        if raw_input("Выключить калькулятор? (да/нет): ") == "да":
            print "Приятного полёта"
            break
