# 1. 文件处理
+ 文件概念
+ 文件打开方式
+ 文件读写操作
+ 文件指针
+ 文件对象属性
+ linux文件系统
+ os模块文件操作
+ 文件练习

# 2. 文件概念
+ 文件：python中文件是对象
+ linux文件：一切设备都可以看成文件
+ 文件属性：用户，读，写，执行

## 2.1 打开文件
+ 文件打开方式：`open(name, [mode[buf]])`
    + name:文件路径
    + mode:打开模式
    + buf: 缓冲buf的大小


mode | 说明 | 注意
---|---|---
'r'|只读方式打开 | 文件必须存在
'w'|只写方式打开 | 文件不存在创建文件，文件存在则清空文件内容
'a'|追加方式打开 | 文件不存在创建文件
'r+/w+'|读写方式打开 | 
'a+'|追加和读写方式打开|
'rb','wb','ab','rb+','wb+','ab+'|二进制方式打开|

+ 文件读取方式
    - `read([size])`读取文件(读取size个字节，默认读取全部)
    - `readline([size])`读取一行
    - `readlines([size])`读取完文件，返回每一行所组成的列表，弊端是占据很大的内存
    - `iter`使用迭代器读取文件`iter(open('./1.txt', 'r'))`
+ 文件写入方法
    - `write(str)`将字符串写入文件
    - `writelines(sequence_of_strings)`写多行文件
+ 写磁盘时机
    - 主动调用`close()`或者`flush()`方法，写缓存同步到磁盘
    - 写入数据量大于或者等于写缓存，写缓存同步到磁盘

+ 文件为什么要关闭
    - 将写缓存同步到磁盘
    - linux系统中每个进程打开文件的个数是有限的
    - 如果打开文件数量到了系统限制，再打开文件就会失败

+ 写入和读取问题
    - 写入文件后，必须打开才能读取写入内容
    - 读取文件后，无法重新再次读取读过的内容


# 3. 文件指针
+ 文件读取写入文件指针移动
+ 文件指针操作`seek(offset, [whence])`移动文件指针
    - `offset`偏移量，可以为负数
    - `whence`偏移相对位置
+ 文件指针定位方式
    - `os.SEEK_SET`相对文件起始位置，0
    - `os.SEEK_CUR`相对文件当前位置，1
    - `os.SEEK_END`相对文件结尾位置，2
+ `f.tell()`返回当前文件的偏移

```python
f = open('./1.txt', 'r+')
import os
print(f.read(4))
print(f.tell())
# 文件指针归位
f.seek(0, os.SEEK_SET)
print(f.tell())
```

# 4. os
+ 文件对象属性
+ 标准文件
+ 文件命令行参数
+ 文件编码格式

## 4.1 文件对象属性
+ `file.fileno()`文件描述符
+ `file.mode`文件打开权限
+ `file.encoding`文件编码格式
+ `file.closed`文件是否关闭

```python
f = open('./1.txt', 'r+')
print(f.fileno())
print(f.mode)
print(f.encoding)
print(f.closed)
```

## 4.2 标准文件
+ `sys.stdin`文件标准输入
+ `sys.stdout`文件标准输出
+ `sys.stderr`文件标准错误

## 4.3 命令行参数
+ `sys`模块提供`sys.argv`属性，通过该属性可以得到命令行参数
+ `sys.argv`字符串组成的列表

## 4.4 文件编码格式
+ 把`unicode`编码转成`utf-8`
+ `unicode.encode(u'你好', 'ytf-8')
+ 使用`codecs`模块提供方法创建指定编码格式文件
+ `open(file,, mode, encoding, errors, buffering)`
