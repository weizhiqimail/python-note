# -*- encoding: utf-8 -*-

from collections.abc import Mapping, MutableMapping

a = {}

print(isinstance(a, Mapping))
print(isinstance(a, MutableMapping))

# a 不是继承了 MutableMapping，只是实现了 MutableMapping 内部的一些魔法函数
