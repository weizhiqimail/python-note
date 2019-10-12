# -*- encoding: utf-8 -*-

age = input('age: ')
age = int(age)
if age >= 18:
    print('your age is ', age)
elif age >= 6:
    print('you are teenager')
else:
    print('you are child')

names = ['mark', 'sherry', 'tom']
for name in names:
    print(name)

num = list(range(1, 21))
sum = 0

for x in num:
    if x % 5 == 0:
        sum += x
    else:
        continue

print(sum)
