# -*- encoding: utf-8 -*-


class Company:
    def __init__(self, employee_list, users):
        self.emloyees = employee_list
        self.users = users

    # 可以直接对实例进行 for 循环，获取到值
    # 实际上是把实例转成一个可迭代对象
    def __getitem__(self, item):
        print('__getitem__ item: ', item)
        return self.emloyees[item]

    def __len__(self):
        return len(self.emloyees)

    # 开发模式下可以用到，在 jumpter 里，直接输入值是可以输出结果的，但是如果是引用数据类型，输出的是地址，不是指
    # 可以用这个魔法函数来修改输出变量的值
    def __repr__(self):
        return ','.join(self.emloyees)


c = Company(['tom', 'merry', 'jane'], [1, 2, 3, 4])
# emloyees = c.emloyees
# for employee in emloyees:
#     print(employee)
print('--------------c--------------------')
print(c)
print('--------------list(c)--------------------')
print(list(c))
print('--------------len(c)--------------------')
print(len(c))

print('--------------for e in c--------------------')
for e in c:
    print(e)


class Number:
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)


n = Number(-3)
# print(abs(n))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        v = Vector(self.x + other.x, self.y + other.y)
        return v

    def __str__(self):
        return "x: {x}, y: {y}".format(x=self.x, y=self.y)


f = Vector(1, 2)
s = Vector(3, 4)
# print(f + s)
