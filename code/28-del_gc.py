# -*- encoding: utf-8 -*-

a = object()

b = a

print(b)

del a

print(b)
print(a)
