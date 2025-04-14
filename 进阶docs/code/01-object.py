# -*- encoding: utf-8 -*-

def ask(name='mark'):
    print(name)


# ask()
ask_2 = ask


# ask_2()


class Person:
    def __init__(self):
        print('mark person')


# P = Person
# P()

l = []

l.append(ask)
l.append(Person)

for item in l:
    print(item())


def decorator_func():
    print('dec start')
    return Person


my_ask = decorator_func()
my_ask()
