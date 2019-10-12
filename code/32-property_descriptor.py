# -*- encoding: utf-8 -*-
import numbers


class IntField(object):

    def __get__(self, instance, owner):
        if self.value:
            return self.value
        return None

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if value < 0:
            raise ValueError('positive value need')
        self.value = value

    def __delete__(self, instance):
        if self.value:
            del self.value


class User:
    age = IntField()

    def __init__(self):
        self.name = 'mark'


class NoDataIntField:
    def __get__(self, instance, owner):
        return self.value


'''
如果 user 是某个类的实例，那么 user.age 等价于 getattr('user', 'age')
首先调用 __getattribute__。如果类定义了 __getattr__ 方法
那么在调用 __getattribute__ 抛出 AttributeError 的时候就会调用到 __getattr__
而对于描述符 __get__ 的调用，则是发生在 __getattribute__ 内部的
user = User()，那么 user.age 的调用顺序

1. 如果 age 是出现在 User 或其基类的 __dict__ 中，且 age 是 data descriptor ，那么调用其 __get__ 方法，否则
2. 如果 age 出现在 user 的 __dict__ 中，那么直接返回 obj.__dict__['age']，否则
3. 如果 age 出现在 User 或其基类的 __dict__ 中
3.1 如果 age 是 non-data descriptor ，那么调用其 __get__ 方法，否则
3.2 返回 __dict__['age']
4. 如果 User 有 __getattr__ 方法，调用 __getattr__ 方法，否则
5. 抛出 AttributeError
'''

if __name__ == '__main__':
    user = User()
    user.age = 18
    print(user.__dict__)
    print(getattr(user, 'age'))
