# -*- encoding: utf-8 -*-

from collections.abc import Sized


class Company:
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __len__(self):
        return len(self.employee_list)


c = Company(['tom', 'merry', 'jane'])
print(len(c))

has_len = hasattr(c, '__len__')
print(has_len)

has_iter = hasattr(c, '__iter__')
print(has_iter)

# 检查某个类是否有某个方法
print(isinstance(c, Sized))
