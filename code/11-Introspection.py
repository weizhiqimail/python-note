# -*- encoding: utf-8 -*-


class Person:
    '''
    这里是注释
    '''
    name = 'mark'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name
        self.grade = '一年级'
        self.get_name = self.get_name

    @classmethod
    def get_name(cls):
        return 'markmam'


s = Student('慕课网')
# 通过 dict 查询属性
print(s.__dict__)
s.__dict__['address'] = '上海市'
print(s.__dict__)
print(s.name)
print(Person.__dict__)
print(dir(Person))
