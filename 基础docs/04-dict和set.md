# 1. dict
+ dict 全称 dictionary，在其他语言中也成为 map，使用键值存储，具有极快的查找速度

```python
user = {
    'mark': 18,
    'tim': 19,
    'jack': 18
}
```

+ dict 查找速度快的原因是，dict 的实现原理和查字典是一样的，先在字典的索引表里查这个字对应也页面，然后直接翻到该页，找到这个字。
+ 可以添加元素 user['sherry'] = 18
+ 在获取元素的值的时候，如果没有这个元素，那么就会报错，通过get()方法，参数为 key ，如果 key 不存在，返回 None 
+ 删除一个 key ，使用 pop(key) 方法，对应的 value 也会从dict中删除
+ dict 的特点(以空间换时间)
    - 查找和插入的速度快，不会随着 key 的增加而变慢
    - 需要占用大量的内存，内存浪费多
+ list 的特点
    - 查找和插入的时间随着元素的增加而增加
    - 占用空间少，浪费内存少
+ dict 可以用在需要高速查找的很多地方，正确使用dict非常重要，dict的 key 必须是不可变对象。因为dict根据 key 来计算 value 的存储位置，如果每次计算相同的 key 得出的结果不同，那么 dict 的内部就会乱掉，这个通过 key 计算位置的算法成为哈希算法。要保证hash的正确性，作为 key 的对象就不能变，在python中，字符串整数都是不可变的，所以可以放心使用。而list是可变的，所以不能作为 key 

# 2. set
+ set是一组key的集合，无序和无重复元素的集合，不存value，由于key不能重复，所以在set中没有重复的元素。
+   s = set([1, 2, 3, 4]) 传入的参数是list，而显示的是 {1, 2, 3, 4} 
+ 添加元素:  add(key) 
+ 删除元素:  remove(key) 
+ 计算两个set的交集:   s1 & s2 
+ 计算两个set的并集:   s1 | s2 

# 3. 不可变对象
+ list内部的顺序会改变

```python
a = ['c', 'b', 'a']
a.sort()
print(a)

# ['a', 'b', 'c']
```
+ str不可变

```python
a = 'ABC'
print(a)
a.replace('A', 'aa')
print(a)

# ABC
# ABC
```