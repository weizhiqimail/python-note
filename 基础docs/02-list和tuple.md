## 1. list
+ list是一种数据类型，是一种有序的集合，可以随时添加和删除其中的元素。
+ 使用`len()`可以获取到list元素的个数
+ 索引是从`0`开始的，也可以使用倒序`-1`来获取最后一个元素，如果没有该索引，那么就会报`IndexError`错误
+ 追加元素使用`append()`
+ 插入元素到指定位置`insert(index, str)`
+ 删除末尾元素使用`pop()`，使用索引参数，删除指定位置的元素
+ 替换某个元素成别的元素，直接修改某个索引的值

```python
user = ['mark', 'jack', 'sherry'];
user.append('tim');
print(user);
print(len(user));

user.pop();
print(user);

user.insert(1, 'merry');
print(user);

user.pop(0);
print(user);

# ['mark', 'jack', 'sherry', 'tim']
# 4
# ['mark', 'jack', 'sherry']
# ['mark', 'merry', 'jack', 'sherry']
# ['merry', 'jack', 'sherry']
```

## 2. tuple
+ 另外一种有序列表，元组，一旦进行初始化，就不能修改，强行修改会报错。
+ 定义一个空的tuple，`t = ();`，为了避免数学计算意义上的括号的歧义，tuple里只有一个元素的时候必须使用` t = (1 ,);`
+ 可变的tuple，` t = (1, 2, [3, 4]);`，在这里边，`1`和`2`不可以改变，但是里边的list的`3`和`4`可以进行修改
