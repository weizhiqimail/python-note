# -*- encoding: utf-8 -*-

l = list(range(1, 21))

for i in l:
    if i % 2 == 1:
        print(i)

ol = map(lambda x: x * x, (i for i in range(21) if i % 2 == 1))

print(list(ol))

d = {
    'mark': 22,
    'sherry': 23,
    'tom': 25
}

rd = {value: key for key, value in d.items()}

print(rd)

# 集合生成式 set
s = {key for key, value in d.items()}
# s = { d.keys() }
print(s)
