# -*- coding:  utf-8  -*-
#-----------------------------------------------

# 查询 x10sql1.py sql2.db


import sqlite3

conn = sqlite3.connect('/home/how/sql/sql2.db')
cursor = conn.cursor()

#执行查询语句

cursor.execute("select *from staff where name=?",('Sam',))

date_set = cursor.fetchall()
for row in date_set:
    print(row)


cursor.close()
conn.close()

