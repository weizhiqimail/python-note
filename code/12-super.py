# -*- encoding: utf-8 -*-


class D:
    def __init__(self):
        print('D __init__')


class C(D):
    def __init__(self):
        print('C __init__')
        super().__init__()


class B(D):
    def __init__(self):
        print('B __init__')
        super().__init__()


class A(B, C):
    def __init__(self):
        print('A __init__')
        super().__init__()


a = A()
print(A.__mro__)
