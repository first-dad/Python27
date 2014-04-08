# -*- coding: utf-8 -*-
'''
name = 'Alex'
print "%(name)s" % vars ()

d,i - число целое
u - беззнаковое число
f - число с плавающей точкой <->m.dddddd
e или E(размер строки. строчная или заглавная) - <->m.dddddd +- e
g,G - выборочный формат
s - строка
r - repr()
c - единственный символ
% - "%%"
'''

'''
d = {"name":"Uriy","height":178}
print "%(name)s : %(height)d" % d
'''


'''
cars = ({"model":"Lada","color":"green","cost":164654.56564},{"model":"bmw","color":"blue","cost":46256.54},{"model":"Mers","color":"red","cost":2654684.65468})
for car in cars:
    print "%-10s | %10s | %6.2d" % (car["model"],car["color"],car["cost"])
'''

'''
if __name__ == '__main__':
    data = [
        'name',
        '123',
        '23.23',
        ' ',
        'SDSDFD',
        ' sdfsdf ',
        'Tdfgdfgdfg',
        '34h5jh3jk4'
    ]

    print '%15s | isalpha | isdigit | islower | istitle | isalnum ' % 'имя'
    print '-------------+---------+---------+---------+---------+--------'
    for value in data:
        print '%12s | %7s | %7s | %7s | %7s | %7s' \
              % (value, value.isalpha(), value.isdigit(),
                 value.islower(), value.istitle(), value.isalnum())
'''

#
# print '{0} {1}'. format("GFJY",2)
# print '{name} {age}' . format(name = 'Bon',age = 6)
# stock = {'name':'Alla','city':'Texas'}
# print '{0[name]} живёт в {0[city]}' . format(stock)


# a.decode                В начале нужно decode из какой-то кодировки в юникод, а затем encode в другою кодировку
# f.write(a.encode('cp1251'))     перекодирование строки
#
# import codecs
# f = codecs.open ('file',encoding='utf-8')
# f2 = open('..')
# ef = codecs.Encoded File(f2, inputenc, outputenc)

