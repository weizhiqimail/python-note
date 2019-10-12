# -*- encoding: utf-8 -*-

def add(x, y, f):
    return f(x) + f(y)


print(add(1, -2, abs))

r = map(abs, list(range(-10, 11)))

print(list(r))

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('4551471'))
