# -*- encoding: utf-8 -*-


class Cat:
    def say(self):
        print('i am cat')


class Dog:
    def say(self):
        print('i am dog')


class Duck:
    def say(self):
        print('i am duck')


animals = [Cat, Dog, Duck]

for animal in animals:
    animal().say()

a = ['mark1', 'mark2', 'mark3']
b = ['mark4', 'mark5', 'mark6']

n_tuple = ['mark1', 'mark2']
n_set = set()
n_set.add('markA')
n_set.add('markB')
a.extend(n_set)
print(a)
d = Dog()


def f(a, b) -> int:
    if a is not None:
        return len(a)
    if b is not None:
        return len(b)
    return 0


s = f([1, 2, 3], [4, 5, 6])
print(s)
s = f(None, None)
print(s)
