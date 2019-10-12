# -*- encoding: utf-8 -*-

user = {
    'home': 'shanghai',
    'name': 'mark',
    'age': 18
}

value = user.get('home')

if value:
    print(value)
else:
    print(None)

value = user.get('school')

if value:
    print(value)
else:
    print(None)

s = {1, 2, 3, 4}
print(s)

s.add(5)
print(s)

s.remove(2)
print(s)

s = set([1, 2, 3, 4])
q = set([3, 4, 5, 6])

print(s & q)
print(s | q)

a = ['c', 'b', 'a']
print(a)

a.sort()
print(a)
