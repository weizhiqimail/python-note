# -*- encoding: utf-8 -*-
import copy

a = {
    'merry': {
        'home': 'shanghai'
    },
    'jack': {
        'home': 'beijing'
    }
}

print(a)
# a.clear()
# print(a)
b = a.copy()
# a['merry']['age'] = 18
b['merry']['home'] = 'SHANGHAI'
print(a)
print(b)

c = copy.deepcopy(a)
print(c)
a['merry']['age'] = 18
print(a)
print(c)

nl = ['merry', 'sherry', 'tom']
nd = dict.fromkeys(nl, {'company': 'imooc'})
print(nd)
