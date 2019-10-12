+ datetime是处理日期和时间的标准库

# 1. 获取当前的日期和时间
+ `datetime`是模块，`datetime`模块包含了一个`datetime`类，通过`from datetime import datetime`导入的才是`datetime`这个类
+ 如果仅仅导入`import datetime`，则必须引用全名`datetime.datetime`
+ `datetime.now()`返回当前日期和时间，类型是`datetime`

```python
from datetime import datetime

now = datetime.now()
print(now) # 2018-07-17 11:25:25.173859
print(type(now)) # <class 'datetime.datetime'>
```

# 2. 获取指定日期和时间
+ 指定某个日期和时间，用参数构造一个`datetime`

```python
from datetime import datetime

time = datetime(2018, 7, 16, 12, 25, 47)
print(time) #  2018-07-16 12:25:47
```
# 3. `datetime`转换为`timestamp`
+ 注意`timestamp`是一个浮点数，如果有小数位，小数位表示毫秒数

```python
from datetime import datetime
time = datetime(2018,7,17,12,25,58)
time.timestamp()
```

# 4. `timestamp`转换为`datetime`
+ `timestamp`没有时区概念，`datetime`有时区概念
+ 本地时间是指当前操作系统设定的时区，比如北京时间
+ 实际上就是UTC+8:00时区的时间

```python
s = 1531801558.0
datetime.fromtimestamp(s)
print(s)
# 2018-07-17 12:25:58
```
+ `timestamp`可以直接被转换到UTC标准时区的时间

```python
s = 1531801558.0
print(datetime.utcfromtimestamp(s))
# 2018-07-17 04:25:58
```

# 5. `str`转换为`datetime`
+ 转换方法是通过`datetime.strptime()`，需要一个日期和时间的格式化字符串

```python
time = datetime.strptime('2018-07-17 12:25:58', '%Y-%m-%d %H:%M:%S')
print(time)

# 2018-07-17 12:25:58
```

# 6. `datetime`转换为`str`
+ 转换方法是通过`serftime()`，需要一个日期格式件的格式化字符串

```python
from datetime import datetime
now = datetime.now()
now.strftime('%a, %b %d %H:%M')
# Tue, Jul 17 11:41
```

# 7. `datetime`加减
+ 加减可以直接用`+`和`-`运算符，需要导入`timedelta`这个类

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=10, hours=15))
```

# 8. 本地时间转为UTC时间
+ 本地时间是指系统设定的时间，UTC时间是指国际标准时间
+ 一个`datetime`类型有一个时区属性`tzinfo`，默认为`None`，所以无法区分这个`datetime`是哪个时区，所以需要给`datetime`设置一个时区

```python
from datetime import datetime, timedelta, timezone
utc8 = timezone(timedelta(hours=8))
print(utc8)
# datetime.timezone(datetime.timedelta(0, 28800))

now = datetime.now()
print(now)
# datetime.datetime(2018, 7, 17, 12, 25, 54, 68578)

dt = now.replace(tzinfo=utc8)
print(dt)
# datetime.datetime(2018, 7, 17, 12, 25, 54, 68578, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
```
# 9. 时区转换
+ 通过`utcnow()`拿到当前的UTC时间，在转换为任意时区的时间
