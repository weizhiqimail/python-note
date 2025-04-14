# -*- encoding: utf-8 -*-

user = 'user'
company = 'company'


def create_class(name):
    if name == user:
        class User:
            def __str__(self):
                return user

        return User
    elif name == company:
        class Company:
            def __str__(self):
                return company

        return Company


if __name__ == '__main__':
    Mu = create_class(user)
    m = Mu()
    print(m)
    print(type(m))
