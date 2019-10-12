# 1. [dict 的 abc 继承关系](../code/22-collections_abc.py)
+ dict 的实例不是继承了 MutableMapping，只是实现了 MutableMapping 内部的一些魔法函数

# 2. [dict的常用方法](../code/23-dict.py)
+ copy 方法，dict 的 copy 方法是浅拷贝，如果需要深拷贝，需要引入 copy，使用 copy.deepcopy
+ dict 的静态方法，使用 fromkeys 可以把可迭代对象转为 dict

# 3. [set](../code/24-set.py)
+ set 是集合
+ fronzenset 是不可变集合，最大的好处是可以作为 dict 的可以，因为不可变
+ set 不能够有重复元素

# 4. [dict和set的原理](../code/25-dict_set.py)
+ dict 查找的性能远远大于 list
+ list 中，随着 list 的数据量变大，查找时间也会变大
+ 在 dict 中，查找时间不会随着 dict 的增大而增大
+ dict 的效率高是因为采用的是哈希表
+ 对于不可变对象，都是可哈希的，比如 str, frozenset, tuple
+ 自己实现的类，可以自己实现类的 `__hash__`
+ dict 的内存开销大，因为在 dict 中会有大量的表元，但是查询速度快，效率高
+ 自定义的对象或 python 内部的对象都是用 dict 包装
+ dict 的存储顺序和元素添加顺序有关

