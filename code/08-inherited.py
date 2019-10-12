# -*- encoding: utf-8 -*-

# 菱形继承关系


'''

class D:
    pass


class B(D):
    pass


class C(D):
    pass


class A(B, C):
    pass


print(A.__mro__)

'''


class D:
    pass


class B(D):
    pass


class E:
    pass


class C(E):
    pass


class A(B, C):
    pass


print(A.__mro__)
