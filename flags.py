# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    data = 'kjhllk 15.04.1236 uih53hkh 45.02.5896ygl'
    pattern = r'(\d{2}).(\d{2}).(\d{4})'

    data = re.compile(pattern).search(data).groups()
    print '{0}-{1}-{2}'.format(data[2], data[1], data[0])
