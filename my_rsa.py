# -*- coding: utf-8 -*-


def is_prime(num):
    for n in range(1, 9):
        if num % n == 0 and (num / n != 1 and num == n):
            return False

    return True


def check(x, y):
    for num in range(x, y):
        if is_prime(num):
            print num


"""
def prime():
    p = []
    for x in range(1, 9):
        for y in range(1, 9):
            if x / y == 0:
            if x / y == 1:
                p.append(x)
            else:
                pass
    print p
"""

if __name__ == '__main__':
    check(1, 30)