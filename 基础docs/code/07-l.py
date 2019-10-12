# -*- encoding: utf-8 -*-

print(list(range(1, 11)))

l = [x * x for x in range(1, 11) if x % 2 == 0]

print(l)

p = [m + n for m in 'ABC' for n in '123']
print(p)

import os

o = [d for d in os.listdir('.')]
print(o)

o = [d for d in os.listdir('..')]
print(o)

o = [d for d in os.listdir('../../')]
print(o)

d = {
    'name': 'mark',
    'age': '18',
    'home': 'china'
}

u = [k + '=' + v for k, v in d.items()]
print(u)

g = (x * x for x in range(1, 11))

for n in g:
    print(n)
