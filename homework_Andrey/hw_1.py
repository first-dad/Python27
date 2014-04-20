# -*- coding: utf-8 -*-


from os import listdir


def result(search, data):
    search = search.lower()
    count = 0

    for line in data:
        words = line.split()

        for word in words:
            index = word.lower().find(search)

            if index > -1:
                count += 1

    return count


def main():
    dir = 'data'
    exit = 'txt'
    search = 'better'

    for name in listdir(dir):
        if name.split('.')[-1] == exit:
            file = open('%s/%s' % (dir, name), 'r')

            number = result(search, file)

            print 'Кол-во слов "%s" в файле %s: %d' % (search, name, number)



if __name__ == '__main__':
    main()