# -*- encoding: utf-8 -*-


class Date:

    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year, month=self.month, day=self.day)

    def tomorrow(self):
        self.day += 1

    # @staticmethod 静态方法如果修改了类名，那么调用了类的方法的地方都要修改，所以可以使用 @classmethod
    # @staticmethod
    # def parse_form_string(date_str):
    #     year, month, day = tuple(date_str.split('-'))
    #     return Date(int(year), int(month), int(day))

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


if __name__ == '__main__':
    date_str = '2019-08-18'
    new_day = Date.from_string(date_str)
    print(new_day)
    print(Date.valid_str(date_str))
