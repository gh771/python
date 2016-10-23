# -*- coding:  utf-8  -*-
# ------------------------------

''''---------------------with语句上下文管理器取  -- 对文件内容进行迭代-------------'''''

print('----------------------------with语句 上下文管理器----------------------------')
#在使用 python编程中会经常碰到这种情况，有一个特殊的语句快，在执行这个语句块之前需要先执行一些准备工作
#当语句块执行完成后，需要继续执行一些收尾动作
#对于这些情况，可以通过上下文管理器(Context Manager)来定义/控制代码块执行前的准备动作，以及执行后的收尾动作

import time 

class Mytimer():
	def __init__(self, verbose=False):
		self.verbose = verbose
	
	def __enter__(self):
		self.start = time.time()
		return self

	def __exit__(self, *unused):
		self.end = time.time()
		self.secs = self.end - self.start
		self.msecs = self.secs * 1000
		if self.verbose:
			print("elapased time: %f ms" %self.msecs)

def fib(n):
	if n in [1,2]:
		return 1
	else:
		return fib(n-1) + fib(n-2)

with Mytimer(True):
	print(fib(30))
	print("Hello world")
	print(time.sleep(3))
 

#832040
#Hello world
#elapased time: 397.964001 ms

print('-------------------------------------------------------------')

import time 

class Mytime(object):
	def __init__(self, verbose = False, ignoreException = False):
		self.verbose = verbose
		self.ignoreException = ignoreException
	
	def __enter__(self):
		self.start = time.time()
		return self
	
	def __exit__(self, *unused):
		self.end = time.time()
		self.secs = self.end - self.start
		self.msecs = self.secs * 1000
		if self.verbose:
			print("elapsed time: %f ms" %self.msecs)
		return self.ignoreException


try:
	with Mytime(True, False):
		raise Exception("Ex4Test")
except Exception as e:
	print("Exception (%s) was caught" %e)
else:
	print("No Exception happened")


#elapsed time: 0.003099 ms
#Exception (Ex4Test) was caught

print('----------------------------------对文件内容进行迭代-----------------------------------------')

# 对文件内容进行迭代

#按字节处理
def process(string):
	print("Processing:" , string)

f = open('/home/how/test2/y7')

while True:
	char = f.read(1)
	if not char: break
	process(char)

#Processing: 对

f.close()

#按行操作

g = open('/home/how/test1/t10')

while True:
	line = g.readline()
	if not line: break
	process(line)

#Processing: #x7file.py t10
g.close()

#用read()迭代每个字符

f = open('/home/how/test2/y7')
for char in f.read():
	process(char)
#Processing: 文
f.close()

#用 readlines迭代行

g = open('/home/how/test1/t10')

for line in g.readlines():
	process(line)
#Processing: discuss the world situation
g.close()

#使用 fileinput模块
import fileinput
for line in fileinput.input('/home/how/test1/t10'):
	process(line) #Processing: her behaviour deeply troubled me


print('--------------------------------文件迭代器----------------------------')

#在 python 从2.2开始，文件对象是可迭代的，这就意味着可以直接在for循环中使用它们

f = open('/home/how/test1/t10')
for line in f:
	print(line)
f.close()

#对文件对象进行迭代 而不使用变量存储文件对象
# 没有把一个打开的文件赋给变量，因此也就没有办法显式地关闭文件

for line in open('/home/how/test1/t9'):
	process(line)




'''
#sys.stdin 是可迭代的就像其他文件对象
import sys
for line in sys.stdin:
	process(line)'''


#可以对文件迭代器执行和普通迭代器相同的操作 比如将他们转换为字符串列表
# 使用 list(open(filename)) 这样所达到的效果和使用readlines一样

y = open('/home/how/test2/y8.txt', 'w')

y.write('First line\n')
y.write('Second line\n')
y.write('Third line\n')
y.close()

lines = list(open('/home/how/test2/y8.txt'))
print(lines) #['First line\n', 'Second line\n', 'Third line\n']

frist, second,third = open('/home/how/test2/y8.txt')

print(frist, second, third)#First line .....


