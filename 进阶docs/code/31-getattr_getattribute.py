# -*- encoding: utf-8 -*-
from datetime import date, datetime


class User:
    def __init__(self, name, birthday, info=None):
        if info is None:
            info = dict()
        self.name = name
        self.birthday = birthday
        self.info = info

    # def __getattr__(self, item):
    #     print('__getattr__')
    #     return self.info[item]

    def __getattribute__(self, item):
        return ''


if __name__ == '__main__':
    user = User('mark', date(year=2010, month=8, day=21), info={'company': 'imooc'})
    # print(user.name)
    # print(user.age)
    print(user.company)
