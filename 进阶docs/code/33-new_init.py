# -*- encoding: utf-8 -*-


class User:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print('name', name)


user = User('mark')
print(user.name)
