# -*- encoding: utf-8 -*-
import math


def myAbs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('ERROR ARGUMENTS')
    if x >= 0:
        return x
    else:
        return -x


a = myAbs(-10)
print(a)


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


print(move(2, 5, 10, 45))


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))


def person(name, age, **kw):
    print('name: ', name)
    print('age: ', age)
    print('kw: ', kw)


person('mark', 18, city='shanghai', school='A school')


def person(name, age, *, city, job):
    print('name: ', name)
    print('age: ', age)
    print('city: ', city)
    print('job: ', job)


work = {
    'city': '上海',
    'job': 'teacher'
}

person('mark', 18, city=work['city'], job=work['job'])


def f1(a, b, c=0, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


f1(1, 2, 3, 'name', 'age', home='shanghai', age=18)


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


s = fact(5)
print(s)


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    else:
        return fact_iter(num - 1, num * product)


print(fact(5))
