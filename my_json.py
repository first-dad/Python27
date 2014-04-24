# -*- coding: utf-8 -*-


from json import dump


if __name__ == '__main__':
    my_dict = {1: "all", 2: "best", 3: "worse"}
    x = open('my_json1.json', 'w')
    dump(my_dict, x)