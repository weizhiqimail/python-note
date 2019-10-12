# -*- encoding: utf-8 -*-


class OriginA:
    name = 'OriginA name'


class A(OriginA):
    name = 'A name'

    def __init__(self, x, y):
        self.name = 'self name'
        self.x = x
        self.y = y


a = A(1, 2)
print(a.x, a.y, a.name)
print(A.name)

a.name = 'a name'
print('a.name: ', a.name)
print('A.name: ', A.name)

A.name = 'new A name'

print('a.name: ', a.name)
print('A.name: ', A.name)

OriginA.name = 'new OriginA name'

print(OriginA.name)

A.x = 100

print(a.x, a.y, a.name)
