# -*- coding:  utf-8  -*-
#-----------------------------------------------

import sqlite3

db = r'/home/how/sql/sql2.db' #数据库文件

drp_tb_sq1 = 'drop table if exists staff'
crt_tb_sq1 = """
		create table if not exists staff(
		id integer primary key autoincrement unique not null,
		name varchar(100),
		city varchar(100)
)"""

#连接数据库

con = sqlite3.connect(db)
cur = con.cursor()
#创建表staff
cur.execute(drp_tb_sq1)
cur.execute(crt_tb_sq1)
#插入记录
insert_sq1 = "insert into staff (name,city) values (?,?)"  #?为占位符
cur.execute(insert_sq1, ('Tom', 'New York'))
cur.execute(insert_sq1, ('Frank', 'Los Angeles'))
cur.execute(insert_sq1, ('Kate', 'Chicago'))
cur.execute(insert_sq1, ('Thomas', 'Houston'))
cur.execute(insert_sq1, ('Sam', 'Philadelphia'))
con.commit()

#查询记录
select_sq1 = 'select * from staff'
cur.execute(select_sq1)
#返回一个list, list中的对象类型为tuple
date_set = cur.fetchall()
for row in date_set:
    print(date_set)


cur.close()
con.close()






