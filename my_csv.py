# -*- coding: utf-8 -*-


import csv


if __name__ == '__main__':
    data = csv.reader(open('my_csv1.csv'))
    for num, element in enumerate(data):
        print '{0}....{1}'.format(num, element)