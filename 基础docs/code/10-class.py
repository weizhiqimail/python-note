# -*- encoding: utf-8 -*-

class Student(object):
    def __init__(self, name, scope):
        self.name = name
        self.scope = scope
        self.__name = name
        self.__scope = scope

    def getScore(self):
        print(self.name, self.scope)


s = Student('mark', 18)
