# -*- encoding: utf-8 -*-

a = 1
b = 'abc'
print(type(1))
print(type(int))
print(type(b))
print(type(str))

# type -> int -> 1
# type -> str -> abc
# type -> class -> obj


class Student:
    pass


class MyStudent(Student):
    pass


stu = Student()

print(type(stu))
print(type(Student))
print(int.__bases__)
print(str.__bases__)
print(Student.__bases__)
print(MyStudent.__bases__)
print(type.__bases__)
print(object.__bases__)
print(type(object))

print(list.__class__)  # <class 'type'>
print(list.__bases__)  # (<class 'object'>,)

lst = [1, 2, 3]
print(lst.__class__)  # <class 'list'>
# AttributeError: 'list' object has no attribute '__bases__'
# print(lst.__bases__)
