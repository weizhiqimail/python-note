# -*- encoding: utf-8 -*-
import copy

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
print(a is b)

c = [1, 2, 3]
d = copy.deepcopy(c)
d.append(4)
print(c)
print(d)
print(c is d)
