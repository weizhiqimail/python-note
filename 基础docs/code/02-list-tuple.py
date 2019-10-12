# -*- encoding: utf-8 -*-

user = ['mark', 'jack', 'sherry']

print(user)

user.append('tom')

print(user)

print(len(user))

user.pop()

print(user)

user.append('tom')

print(user)

user.pop(1)

print(user)

t = (1, 2, [3, 4], 5)

print(t[0])
print(t[1])
print(t[2])
print(t[3])
t[2][0] = 7
t[2][1] = 8
print(t[0])
print(t[1])
print(t[2])
print(t[3])
# 报错 t[2] = []
print(t[0])
print(t[1])
print(t[2])
print(t[3])
