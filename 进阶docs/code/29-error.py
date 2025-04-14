# -*- encoding: utf-8 -*-

def add(a, b):
    a += b
    return a


# 参数为数字
a = 1
b = 2
c = add(a, b)
print(a, b, c)

# 参数为 list
a1 = [1, 2]
b1 = [3, 4]
c1 = add(a1, b1)
print(a1, b1, c1)

# 参数为 tuple
a2 = (1, 2)
b2 = (3, 4)
c2 = add(a2, b2)
print(a2, b2, c2)


class Company:
    def __init__(self, name, stuffs=[]):
        self.name = name
        self.stuffs = stuffs

    def add(self, stuff_name):
        self.stuffs.append(stuff_name)

    def remove(self, stuff_name):
        self.stuffs.remove(stuff_name)


stuffs = ['mark', 'tom', 'sherry']

c1 = Company('c1', stuffs=stuffs)
c1.add('merry')
c1.remove('tom')
print(c1.stuffs)

c2 = Company('c2')
c2.add('merry')

c3 = Company('c3')
c3.add('tim')

print(c2.stuffs)
print(c3.stuffs)
print(c2.stuffs is c3.stuffs)
print(Company.__init__.__defaults__)
# c2 和 c3 实际上都使用了默认的空的 list
# 这个默认值可以通过 Company.__init__.__defaults__
