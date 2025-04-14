# -*- encoding: utf-8 -*-


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)

    def tomorrow(self):
        self.day += 1

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0 and 0 < int(month) <= 12 and 0 < int(day) <= 31:
            return True
        return False


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2019 - self.__birthday.year


class Student(User):

    def __init__(self, birthday):
        self.__birthday = birthday


user = User(Date(1990, 1, 1))
print(user.get_age())
print(user._User__birthday)
