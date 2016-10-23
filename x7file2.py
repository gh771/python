# -*- coding:  utf-8  -*-
#-----------------------------------------------

'''----------------------os模块操作目录--- 流位置-----------------------'''

# os 模块 操作文件和目录
# 操作系统提供的命令只是简单地调用操作系统提供的接口函数， python内置的 os 模块也可以直接调用操作系统提供的接口函数

import os 
print(os.name) # posix

print(os.uname()) #posix.uname_result(sysname='Linux'........

# os.environ # 对当前环境变量进行映射
print(os.environ.get('PYTHONPATH'))# 获取某个环境变量的值
print(os.environ.get('PATH'))
#print(os.environ) 全部环境变量

# 查看当前目录的绝对路径
print(os.path.abspath('.')) #/home/how/python1

#在某个目录下创建一个新的目录，首先把新目录的完整路径表示出来
print(os.path.join('/home/how/python1', 'x8.py')) #/home/how/python1/x8.py
'''把两个路径合成一个时，不要直接拼字符串而要通过 os.path.join()函数，这样可以正确处理不同操作系统的
路径分隔符'''

#创建一个目录
#os.mkdir('/home/how/python1/x8.py')
#os.mkdir('/home/how/python1/x9.txt')
# 删掉一个目录
#os.rmdir('/home/how/python1/x8.py')
#os.rmdir('/home/how/python1/x9.txt')


#在拆分路径的时候 也不要直接取拆字符串，要通过 os.path.split() 函数 
#这样可以把一个路径分为两部分，后一部分总是最后级别的目录或文件名

print(os.path.split('/home/how/python1/x8.py'))# ('/home/how/python1', 'x8.py')

# os.path.split() 可以让你直接得到文件扩展名
print(os.path.splitext('/home/how/python1/x9.txt')) # ('/home/how/python1/x9', '.txt')

# 这些合并 拆分路径的函数并不要求文件和目录真实存在，它们只对字符串进行操作

# 对文件重命名
#os.rename('/home/how/python1/pp.py', 'ppp.py')
#删掉文件
#os.remove('ppp.py')


import shutil

#shutil.copy  拷贝文件的时候确认目录存在
#shutil.copy('/home/how/test2/y8.txt', '/home/how/test2/y9')

# shutil.move  移动文件或文件夹到另一个地方
#shutil.move('/home/how/python1/y10', '/home/how/test2')

# shutil. copyfile(src,dst) # 拷贝文件
#shutil.copyfile('/home/how/test2/y9', '/home/how/test2/y10.txt')





# 利用python特性来过滤文件

import os

print([x for x in os.listdir('.') if os.path.isdir(x)])

#列出当前目录下所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

'''
#指定编码读取相应的数据，忽略非法编码

with open('somefile.txt', 'r', encoding = 'gbk', errors = 'igonre') as f1:
    for line in f1.readlines():
        print(line.strip())

'''


print('----------------------------流位置 the stream position---------------------------------')
from io import StringIO

''' 使用 tell()查看流位置， 使用seek()调整流位置'''

f = StringIO()
print(f.tell()) # 0
f.write('the stream position')
print(f.tell()) #19
s = f.readlines()
print(s) #[]

print('---------------------------------------------')

d = StringIO('a long thin board') #当使用Str时流位置为0
print(d.tell()) # 0
print(d.readline()) #a long thin board #执行后流位置为17
print(d.readline())                #再次执行时返回空
print(d.tell()) #17
print('-------------------------------------------------')

f1 = StringIO()
print(f1.tell()) # 0  # 流位置为0
f1.write(" be brought up by aunt") # 执行后流位置为22
print(f1.tell()) # 22
f1.seek(0)     #  使用seek()调整流位置
print(f1.tell()) # 0
s = f1.readlines()  #输出结果

print(s) #   [' be brought up by aunt']














