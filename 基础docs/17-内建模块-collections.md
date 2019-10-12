+ `collections`是内置的一个集合模块，提供了许多有用的集合类。

# 1. collections模块
+ tuple
+ namedtuple
+ defaultdict
+ deque
+ Counter
+ OrderedDict
+ ChainMap

# 2. namedtuple
+ `tuple`的好处
    - `immutable` 的重要性，性能优化，线程安全
    - 可以作为 dict 的 key (可哈希才可以作为 key , list 不可以作为哈希的 key )
    - 和 C 语言对比，`tuple` 对应的是 `struct`，`list` 对应的是 `Array`
    - `tuple` 可以拆包

```python
from collections import namedtuple

user = ('mark', 18, 175)
name, age, height = user
print(name)
print(age)
print(height)

# 拆包
name, *others = user
print(name)
print(others)

User = namedtuple('User', ['name', 'age', 'height'])
sherry = ('sherry', 18, 25)
user = User(*sherry)
```
+ `tuple` 可以表示不变集合，例如一个点的二维坐标就可以表示成 `p = (1, 2)`
+ 但是我们很难把 `(1, 2)` 看做是一个坐标，所以可以使用 `namestuple`
+ `namedtuple` 是 `tuple` 的一个子类，如果对比 `class`，`namedtuple` 就会节省空间

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)   #  Point(x=1, y=2)
print(p.x) # 1
print(p.y) # 2

User = namedtuple('User', ['name', 'age', 'height'])
user = User('sherry', 18, 25)
print(user)
```
+ `namedtuple` 是一个函数，用来创建一个自定义的 `tuple` 对象，并且规定了 `tuple` 的个数，可以用属性而不是索引来引用 `tuple` 的某一个元素
+ `namedtuple` 可以很方便地定义一种数据类型，具备 `tuple` 的不变性，又可以根据属性来引用。
+ 验证创建的 `Point` 对象是 `tuple` 的一种子类 `isinstance(p, Point)`

# 3. deque
+ 使用 `list` 存储数据时，按照索引访问元素很快，但是插入和删除就很慢，因为 `list` 是线性存储，数据量大的时候，插入和效率很低。
+ `deque` 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
+ `deque` 除了实现 `list` 的 `append()` 和 `pop()` 外，还支持 `appendlift()` 和 `popleft()` ，这样就可以非常高效的往头部添加或删除元素
+ `deque` 是线程安全的，`list` 不是线程安全的

> 在线程里面，线程共享进程里的资源，假设进程里面有一个 list， 如果你开了多个线程去删除它的一个元素，那么它可能可能被一个线程给删了某个元素，但是另一个线程也想删除这个元素，然而它早就被其他线程删除了，这就会引发线程安全问题，也就是说列表是线程非安全的，你可能会问这些线程怎么会操作同一个元素呢，不是被某个线程删了就不会出现在list里了吗？确实，有这种疑问很正常，那是因为线程之间有个东西叫时间片，如果这个时间片用完了就会切换线程对吧，切换时被切换的线程可能还没有完成删除操作就被其他线程占了cpu，然后占了cpu的线程把元素删了，切换回来的时候，那个线程想删，哦，没有了，只能报错，对吧

```python
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('e')
print(q) # deque(['e', 'a', 'b', 'c', 'd'])
```
# 4. defaultdict
+ setdefault

```python
# -*- coding: utf-8 -*-

from collections import defaultdict

users = [1, 2, 3, 4, 5, 6, 7, 8, 9]

d = {}

for user in users:
    if user not in d:
        d[user] = 1
    else:
        d[user] += 1

print(d)

for user in users:
    d.setdefault(user, 0)
    d[user] += 1

print(d)
```

+ defaultdict
+ 使用`dict`时，如果引用的`key`不存在，就会抛出`KeyError`，如果希望`key`不存在时，返回一个默认值，可以使用`defaultdict`
+ 除了在key不存在时返回默认值，`defaultdict`的其他行为跟`dict`完全一样

```python
# -*- coding: utf-8 -*-

from collections import defaultdict

users = [1, 2, 3, 4, 5, 6, 7, 8, 9]

d = defaultdict(int)
for user in users:
    d[user] += 1

print(d)
```
+ `defaultdict`的参数是一个可调用对象，自己写一个函数也是可以的

# 5. OrderedDict
+ Python在2.x版本之下，`dict`是无序的
+ Python在3.x版本下，`dict`和`OrderedDict`都是有序的
+ 使用`dict`时，key是无序的，在对`dict`做迭代的时候，无法确定 key 的顺序
+ 要保持key的顺序，可以使用`OrderedDict`
+ `od.popitem()`移出最后一个元素
+ `od.move_to_end(key)`把元素移到最后的位置

```python
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

print(d)   #  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(od)  #  OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
```
+ `OrderedDict`的key会按照插入的顺序排列，而不是key本身

```python
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)  #  OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```
+ `OrderedList`可以实现一个先进先出的`dict`，当容量超过限制的时候，先删除最早添加的key

```python
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove: ', last)

        if containsKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))

        OrderedDict.__setitem__(self, key, value)

od = LastUpdatedOrderedDict(4)
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(od)
od['e'] = 5
print(od)
```

# 6. Counter计数器
+ `Counter`是`dict`的一个子类
+ `Counter`是一个计数器，可以统计字符出现的个数
+ `Counter.update(x)`添加一些元素
+ `Counter.most_common(n)`出现次数最多的前N个元素


```python
from collections import Counter

c = Counter()
str = 'hello, this is a test message'

for x in str:
    c[x] = c[x] + 1

print(c)

# Counter({' ': 5, 's': 5, 'e': 4, 't': 3, 'h': 2, 'l': 2, 'i': 2, 'a': 2, 'o': 1, ',': 1, 'm': 1, 'g': 1})

```

# 7. ChainMap

```python
from collections import ChainMap

userDict1 = {'a': 'one', 'b': 'two'}

userDict2 = {'c': 'three', 'd': 'four', 'b': 'five'}

newDict = ChainMap(userDict1, userDict2)
print(newDict.maps)
newDict.maps[0]['a'] = 'aaaa'
for key, value in newDict.items():
    print(key, value)

```