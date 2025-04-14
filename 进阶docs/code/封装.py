# -*- encoding: utf-8 -*-
class Auth():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def authticate(self):
        return True


class Request():
    def __init__(self, obj):
        self.obj = obj

    @property
    def user(self):
        return self.obj.authticate()


class APIView():
    def dispatch(self):
        self.f2()

    def f2(self):
        a = Auth('mark', 18)
        req = Request(a)
        print(req.obj)
        print(req.user)


obj = APIView()
obj.dispatch()
