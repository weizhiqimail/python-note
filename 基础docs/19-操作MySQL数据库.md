+ 访问DB的官方接口规范(Python DB API)
+ 开发DB程序的开发环境
+ 访问DB的connection，cursor两大对象
+ 执行增删改查的实例操作

# 1. DB API数据库链接对象connection
+ `pip install PyMySQL`
+ 连接对象：建立Python客户端与数据库的网络连接

参数名 | 类型 | 说明
---|---|---
host | 字符串 | MySQL服务器地址
port | 数字 | MySQL服务器端口号
user | 字符串 | 用户名
passwd | 字符串 | 密码
db | 字符串 | 数据库名称
charset | 字符串 | 连接编码

+ connection对象支持的方法

方法名| 说明
---|---
cursor() | 使用该连接创建并返回游标
commit() | 提交当前事务
rollback() | 回滚当前事务
close() | 关闭连接

+ 示例

```python
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='imooc',
    charset='utf8'
)

cursor = conn.cursor()

print(conn)
print(cursor)

cursor.close()
conn.close()
```

# 2. DB API-数据库游标对象cursor
+ 游标对象：用于执行查询和获取结果
+ `cursor`对象支持的方法

参数名 | 说明
---|---
execute[opt, [,args]]| 执行一个数据库查询和命令
fetchone() | 取得结果集的下一行
fetchmany(size) | 取得结果集的下几行
fetchall()|获取结果集中剩下的所有行
rowcount | 最近一次execute返回数据的行数或者影响行数
close() | 关闭游标对象

+ `execute`方法：执行SQL，将结果从数据库获取到客户端
+ `fetch*`方法，移动`rownumber`，返回数据
+ 示例

```python
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='imooc',
    charset='utf8'
)

cursor = conn.cursor()

sql = 'select * from user'
cursor.execute(sql)

print(cursor.rowcount)

rs = cursor.fetchone()
print(rs)

rs = cursor.fetchmany(3)
print(rs)

rs = cursor.fetchall()
for row in rs:
	print('userid=%s, username=%s' % row)


#  7
#  (1, 'a')
#  ((2, 'b'), (3, 'c'), (4, 'd'))
#  ((5, 'e'), (6, 'f'), (7, 'g'))

cursor.close()
conn.close()
```

# 3. 更新数据
+ 逻辑：
    - 创建`connection`
    - 获取`cursor`
    - 执行`cursor.execute()`的增删改操作
    - 出现异常，使用`conn.rollback()`回滚事务
    - 没有异常，使用`conn.commit()`提交事务
    - 关闭`cursor`
    - 关闭`connection`
+ 事务：访问和更新数据库的一个程序执行单元
    - 原子性：事务中包括的诸多操作要么都做，要么都不做
    - 一致性：事务必须使用数据库从一致性状态变到另一个一致性状态
    - 隔离性：一个事务的执行不能被其他事务干扰
    - 持久性：事务一旦提交，它对数据库的改变就是永久性的
+ 如何使用事务？
    - 关闭自动`commit`：设置`conn.autocommit(False)`
    - 正常结束事务：`conn.commit()`
    - 异常结束事务：`conn.rollback()`

```python
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='imooc',
    charset='utf8'
)

cursor = conn.cursor()

sql_insert = "insert into user(id, name) value (10, 'h')"
sql_update = "update user set id=100 where id=5"
sql_delete = "delete from user  where d < 3"

try:
	cursor.execute(sql_insert);
	print('cursor.rowcount: ', cursor.rowcount);
	cursor.execute(sql_update);
	print('cursor.rowcount: ', cursor.rowcount);
	cursor.execute(sql_delete);
	print('cursor.rowcount: ', cursor.rowcount);
except Exception as e:
	print(e);
	conn.rollback()


conn.commit()

cursor.close()
conn.close()
```

# 4. 转账示例
+ 逻辑
    - 开始事务
    - 检测账户A和账户B是否可用
    - 检测账户A是否有100元
    - 账户A减去100元
    - 账户B加上100元
    - 提交事务
    - 以上任何一个事务出现异常，都会回滚

```python
# coding: utf-8

import pymysql
import sys

class TransferMoney(object):
	def __init__(self, conn):
		self.conn = conn

	def check_acct_available(self, acctid):
		try:
			cursor = self.conn.cursor()
			sql = "select * from account where acctid=" + acctid
			cursor.execute(sql)
			print('check_acct_available: ', sql)
			rs = cursor.fetchall()
			if len(rs) != 1:
				raise Exception('账号%s不存在'%acctid)
		finally:
			cursor.close()

	def has_enough_money(self, acctid, money):
		try:
			cursor = self.conn.cursor()
			sql = "select * from account where acctid=%s and money >%s"%(acctid, money)
			cursor.execute(sql)
			print('has_enough_money: ', sql)
			rs = cursor.fetchall()
			if len(rs) != 1:
				raise Exception('账号%s没有足够的钱'%acctid)
		finally:
			cursor.close()

	def reduce_money(self, acctid, money):
		try:
			cursor = self.conn.cursor()
			sql = "update account set money=money-%s where acctid=%s"%(int(money), acctid)
			cursor.execute(sql)
			print('reduce_money: ', sql)
			if cursor.rowcount != 1:
				raise Exception('账号%s减款失败'%acctid)
		finally:
			cursor.close()

	def add_money(self, acctid, money):
		try:
			cursor = self.conn.cursor()
			sql = "update account set money=money+%s where acctid=%s"%(int(money), acctid)
			cursor.execute(sql)
			print('reduce_money: ', sql)
			if cursor.rowcount != 1:
				raise Exception('账号%s加款失败'%acctid)
		finally:
			cursor.close()

	def check_money(self):
		try:
			cursor = self.conn.cursor()
			sql = "select * from account"
			cursor.execute(sql)
			rs = cursor.fetchall()
			print(rs)
		finally:
			cursor.close()

	def transfer(self, source_acctid, target_acctid, money):
		try:
			self.check_acct_available(source_acctid)
			self.check_acct_available(target_acctid)
			self.has_enough_money(source_acctid, money)
			self.reduce_money(source_acctid, money)
			self.add_money(target_acctid, money)
			self.check_money()
			self.conn.commit()
		except Exception as e:
			self.conn.rollback()
			raise e



if __name__ == '__main__':
	source_acctid = sys.argv[1]
	target_acctid = sys.argv[2]
	money = sys.argv[3]

	print('source_acctid: ', source_acctid)
	print('target_acctid: ', target_acctid)
	print('money: ', money)

	conn = pymysql.connect(
	    host='localhost',
	    port=3306,
	    user='root',
	    password='123456',
	    db='imooc',
	    charset='utf8'
	)
 

	tr_money = TransferMoney(conn)

	try:
		tr_money.transfer(source_acctid, target_acctid, money)
	except Exception as e:
		print('wrong', str(e))
	finally:
		conn.close()
```
