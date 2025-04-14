# -*- encoding: utf-8 -*-

try:
    print('start task')
    # raise KeyError
except KeyError as e:
    print('key error')
else:
    print('else')
finally:
    print('finally')


class A:

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        return self

    def dododo(self):
        print('dododo')


with A() as a:
    a.dododo()
