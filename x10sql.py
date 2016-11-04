# -*- coding:  utf-8  -*-
#-----------------------------------------------
''' 数据库应用示例'''
'''Sqlite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说没有独立的维护进程，
所有的维护都来自程序本身.在python中使用sqlite3创建数据库的连接当我们指定的数据库文件不存在的
时候连接对象会自动创建数据库文件，连接对象可以是硬盘上面的数据文件，也可以是建立在内存中的
在内存中的数据库执行完任何操作后，都不需要提交事务 '''


import sqlite3
##sqlite3只是一个SQLite的接口。
#startswith(str) #检查一个字符串开头是否包括含某段字符串 返回True或 False
# endswith(str) #结尾是否包含某段字符串 返回 True 或 False

def convert(value):
	if value.startswith('~'):
		return value.strip('~')#删除两端~
	if not value:
		value = '0'
	return float(value)
	
conn = sqlite3.connect('/home/how/sql/sqlfood.db')#连接数据库 数据库文件是sqlfood.db
curs = conn.cursor()# 创建一个光标

try:
	curs.execute('''
		create table food(
			id		text primary key,
			desc		text
	)	
	''')
except Exception as e:
	pass

#执行SQL语句 创建food表 主键id desc

query = 'insert into food values (?,?)'#(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)#使用 %s 容易受到SQL注入攻击

for line in open('/home/how/Downloads/LANGDESC.txt'):
	fields = line.split('^')#用^分割字符串成序列
	vals = [convert(f) for f in fields]
	print(vals)
	curs.execute(query, vals)# 执行query 插入值vals
#或者使用 executemany ，然后提供一个从数据文件中提取的所有行的列表，小型程序会带来轻微的速度提升
#如果使用通过网络连接的客户机/服务器SQL系统 会大大的提高速度

curs.close() # 关闭游标对象
conn.commit()# 提交事务
conn.close() #关闭连接















