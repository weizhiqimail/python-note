# -*- encoding: utf-8 -*-
from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

    @age.getter
    def age(self):
        return self._age


if __name__ == '__main__':
    user = User('mark', date(year=2010, month=8, day=21))
    print(user.name)
    print(user.birthday)
    user.age = 23
    print(user.age)
    print(user._age)
