# -*- encoding: utf-8 -*-

# l = list(range(1, 101))
# print(l)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
     11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
     41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
     51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
     71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
     81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
     91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print(l[0:3])
print(l[2:3])
print(l[3:3])
print(l[-5])
print(l[-5:])
print(l[-6:-2])

print(l[0:10:2])
print(l[::2])
print(l[:])


def trim(s):
    if s != '':
        if s[0] == ' ':
            s = trim(s[1:])
        elif s[-1:] == ' ':
            s = trim(s[:-1])
    return s


s = trim('    1235    ')
print(s)
print(len(s))

from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance({1, 2, 3}, Iterable))
print(isinstance({'home': 'shanghai'}, Iterable))

for index, value in enumerate([1, 2, 3, 4]):
    print(index, value)

for x, y, z in [(1, 2, 3), ('A', 'B', 'C'), ('a', 'b', 'c')]:
    print(x, y, z)
