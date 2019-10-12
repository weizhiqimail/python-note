## Python操作CSV

+ 读取CSV文件

```python
# encoding: utf-8

import csv

# with open('user.csv', 'r') as fp:
#     # reader是一个迭代器
#     reader = csv.reader(fp)
#     titles = next(reader)
#     for line in reader:
#         print(line)


# 通过字典的模式读取csv

with open('user.csv', 'r') as fp:
    reader = csv.DictReader(fp)
    for info in reader:
        print(info['Year'], info['Make'], info['Model'], info['Description'], info['Price'])

```

+ 写入CSV文件

```python
# encoding: utf-8

import csv

headers = ['name', 'age', 'home', 'email']
value = [('马克', 18, 'beijing', 'mark@qq.com'),
         ('杰克', 17, 'shanghai', 'jack@qq.com'),
         ('谢丽', 19, 'guangzhou', 'sherry@qq.com')]

# with open('csv_write.csv', 'w', encoding='utf-8', newline='') as fp:
#     file = csv.writer(fp)
#     file.writerow(headers)
#     file.writerows(value)

value = [
    {'name': '马克', 'age': 18, 'home': 'beijing', 'email': 'mark@qq.com'},
    {'name': '杰克', 'age': 17, 'home': 'shanghai', 'email': 'jack@qq.com'},
    {'name': '谢丽', 'age': 19, 'home': 'guangzhou', 'email': 'sherry@qq.com'},
]

with open('csv_write.csv', 'w', encoding='utf-8', newline='') as fp:
    file = csv.DictWriter(fp, headers)
    file.writeheader()
    file.writerows(value)

```

