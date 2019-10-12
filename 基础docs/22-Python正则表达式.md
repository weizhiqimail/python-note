# 1. 正则表达式
+ 使用单个字符串来描述匹配一系列符合某个句法规则的字符串
+ 对字符串操作的一种逻辑公式
+ 应用场景是处理文本和数据
+ 正则表达式过程：依次拿出表达式和文本中的字符比较，如果每一个字符都能匹配，则匹配成功，否则匹配失败

# 2. 匹配单个字符
```python
# encoding: utf-8

import re

# 1. 匹配某一个字符串，从左往右，并且是从第一个位置开始
text = 'ahello'
ret = re.match('he', text)
print(ret)

# 2. 匹配某一个字符串，从字符串的任意一个位置
ret = re.search('he', text)
print(ret.group())

# 3. . 匹配任意的一个字符，不能匹配换行符
ret = re.match('.', text)
print(ret.group())

# 4. \d  匹配任意的一个数字
text = 'hello 123'
ret = re.search('\d', text)
print(ret.group())

# 5. \D  匹配任意的一个非数字
ret = re.search('\D', text)
print(ret.group())

# 6. \s  匹配空白字符， 包括(\n, \t, \r, 空格)
text = ' pi'
ret =  re.search('\s', text)
print(ret.group())

text = '\npi'
ret =  re.search('\s', text)
print(ret.group())

# 7. \w  匹配大小写英文字母，数字，下划线
text = 'A'
ret = re.search('\w', text)
print(ret.group())

# 8. \W, 与\w相反
text = '+'
ret = re.search('\W', text)
print(ret.group())

# 9. []组合，满足[]里的规则就可以匹配的到
text = 'AMERK'
ret = re.search('[ME]', text)
print(ret.group())


text = 'AMERK-141254TEOJYN'
ret = re.search('[\d-]+', text)
print(ret.group())
```
## 3. 匹配多个字符

```python
# encoding: utf-8

import re

# 1. *  匹配0个或任意多个字符
text = '*-/*ahello12664-!@#$%^&*()_+'
ret = re.search('\w*', text)
print(ret.group())

# 2. +  匹配一个或多个字符
text = '+abcd'
ret = re.search('\w+', text)
print(ret.group())

# 3. ? 匹配0个或一个
text = 'yer'
ret = re.search('\w?', text)
print(ret.group())

# 4. {m}匹配m个字符
text = 'uyhhik'
ret = re.search('\w{2}', text)
print(ret.group())

# 5. {m, n}匹配m到n个字符
text = 'uyhhik'
ret = re.search('\w{2,4}', text)
print(ret.group())

```

# 4. 简单的示例

```python
# encoding: utf-8

import re


# 1. 验证手机号

def checkPhoneNumber(number):
    ret = re.match('1[34578]{1}\d{9}', number)
    return ret.group()


# print(checkPhoneNumber('18574741252'))


# 2. 验证邮箱
def checkEmail(email):
    ret = re.match('\w+@[a-z0-9]+\.\w+', email)
    return ret.group()


# print(checkEmail('dsd@dssds.vom'))


# 3. 验证url

def checkURL(url):
    ret = re.match('(http|https|ftp)://[^\s]+', url)
    return ret.group()

# print(checkURL('https://www.google.com/china'))

# 4. 验证1-100数字
def check0TO100(num):
    ret = re.match('[1-9]?\d$|100$', num)
    return ret.group()


print(check0TO100('8'))

```