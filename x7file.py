# -*- coding:  utf-8  -*-
# ------------------------------

'''''----------------- 读写-- 在内存中读写--- 随机访问 ---------------'''''


#open（name[,mode[buffering]]) #open函数使用一个文件名作为唯一的强制参数，然后返回一个文件对象
#模式(mode) 和缓冲(buffering)参数都是可选的
# 
# 'r' 读模式， 'w' 写模式， 'a'追加续写模式， 'b'二进制模式(可添加到其他模式中)，'+'读写模式(可添加到其他模式)
#像open()函数返回的这种有个read()方法的对象，在Python中统称为file like Object(类文件对象)

print('--------------------------- r读模式 -------------------------------------')
f = open('/home/how/test1/t8') # open函数默认读模式
t = open('/home/how/test1/t9')
h = open('/home/how/test1/t10')

print(f.read())#调用read()会一次性读取文件的全部内容

print(t.read(30))# 但是如果文件太大内存就爆了所以可以反复调用read(size)方法， 每次最多读取(size)字节的内容
#x7file.py t9  He has a high fe


print(h.readline())#可以每次读取一行内容 #readline(10) 读取一行的10个字节
#x7file.py t10

print(h.readlines())#一次读取全部内容并且按行返回list
#  ['discuss the world situation\n', 'the road surface has broken up\n', 'her behaviour deeply troubled me \n', 'the theatre was empty\n']
# 第一行 x7file.py t10 被 h.readline() 读取

for line in t.readlines(): print(line.strip())
#ver(前一部分被 t.read(30)读取)\ go to a cinema\ under the bridge

print(f.close(), t.close(), h.close())#文件使用完毕后必须关闭，因为文件对象会占用操作系统资源并且系统同一时间能打开的文件数量也是有限的

with open('/home/how/python1/test0.py', 'r') as g:#每次调用close()太繁琐，使用with语句能自动调用close()方法
    print(g.read()) ## -*- coding:  utf-8  -*- \# ------------------------------ \print('Test0')

print('-------------------- rb 读取二进制--------------------------------')
th = open('/home/how/lmages/th.jpeg','rb')#读取二进制文件，比如图片视频等等
print(th.read())#b'\xff\xd8\xff\xe0\x00\\x00........#十六进制表示的字节


print('--------------------------- w 写模式------------------------------------')

w = open('/home/how/test2/y1.txt','w')
w.write(u'he has a high fever\n')
w.write(u'manage to pass rhe examination\n')
w.write(u'winter is almost over')
w.close() #你可以反复调用write()来写文件，但是务必调用close()来关闭文件，操作系统不会立刻把数据写入磁盘
#而是放到内存缓存起来，空闲时慢慢写入，只有调用close()方法时，操作系统才保证把没有写入的数据写入磁盘

w1 = open('/home/how/test2/y1.txt')
print(w1.read(20)) #he has a high fever
print(w1.read()) #manage to pass rhe examination \winter is almost over


w2 = open('/home/how/test2/y5.txt', 'w')
w2.writelines(['have\t','a\t', 'scarf\n', 'around', 'my', 'neck'])
w2.close()
w3 = open('/home/how/test2/y5.txt')
print(w3.read()) #have	a	scarf \aroundmyneck

sl = ('The', 'ice', 'is','too', 'thin', 'to', 'bear', 'your', 'weight')
w4 = open('/home/how/test2/y5.txt', 'w')
w4.writelines(sl)# writelines 传给它一个序列或者可迭代的对象它会把所有的字符串写入文件
w4.close()
w5 = open('/home/how/test2/y5.txt')
print(w5.read()) # Theiceistoothintobearyourweight


print('----------------------随机访问----------------------------')
#在文件中随意移动读取位置也是可以的，可以使用类文件对象(file-like Object)的方法 seek 和 tell 来直接访问感兴趣的部分(这种做法成为随机访问)
#

#seek(offset[,whence]) #这个方法把当前位置(进行读写的位置)移动到由offset和whence定义的位置
# offset表示字节(字符)数的偏移量 ， whence默认是0,表示偏移量是从文件开头开始计算的(偏移量必须是非负的)
# whence可能被设置为1(相当于当前位置的移动，此时偏移量offset可以是负的)或者2 (相对于文件结尾的移动)

s = open(u'/home/how/test2/y3.txt', 'w')
s.write('0123456789123456789')
s.seek(5)
s.write('different mathods for studying English\n appear on a TV program')
s.close()
s = open(u'/home/how/test2/y3.txt')
print(s.read()) # 01234different mathods for studying English
                #appear on a TV program


print('-------------------------------------')
# tell 方法返回当前文件的位置
s = open(r'/home/how/test2/y3.txt')
print(s.tell())# 0
print(s.read(3)) # 012
print(s.read(10)) # 34different
print(s.tell()) # 13
#tell方法返回的数字在这种情况下时一个长整数，但不是所有的情况都是这样




print('------------------------------------内存中读写数据------------------------------------------')

''''
#字符编码 要读取非 UTF-8编码的文本文件，要给open()函数传入 encoding参数 例如要读取 GBK编码的文件

f = open('somefile.txt', 'r', encoding = 'gbk')

#有些编码不规范的文本文件中可能夹杂了一些非法编码的字符 会抛出UnicodeDecodeError(解码错误)
#遇到这种情况 open() 函数还接收一个 errors参数  表示如果遇到编码错误后如何处理，最简单的方法是直接忽略

f = open('somefile.txt', 'r', encoding = 'gbk', errors = 'ignore')


'''''

print('-----------------------------------StringIO--------------------------')
# StringIO 数据读写不一定是文件 也可以在内存中读写 StringIO就是在内存中读写str

from io import StringIO

f = StringIO()

f.write('Hello ')
f.write('world')
print(f.getvalue())  # Hello world
'''getvalue() 方法用于获得写入后的str'''

# 要读取 StringIO 可以用一个str初始化StringIO 然后像读文件一样读取

f = StringIO('Hello!\nHI!\nGoodbye!')
while True:
    s = f.readline()
    if s == '': break
    print(s.strip())  # strip方法返回去除两侧(不包括内部)空格，也可以指定需要去除的字符，将它们列为参数即可

for line in StringIO('trade\n helps\n industry\n to develop'):
    # print(list(line.strip()))#['t', 'r', 'a', 'd', 'e']
    print(line.strip())  # trade

print('------------------------------BytesIO--------------------------------------')
# BytesIO 如果要操作二进制数据，就需要使用 BytesIO
# BYtesIO 实现了在内存中读写bytes

from io import BytesIO

b = BytesIO()

b.write('中文'.encode('utf-8'))
'''写入的不是str 而是经过UTF-8编码的bytes'''

print(b.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'

b.write('河北 河南'.encode('utf-8'))
print(b.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87\xe6\xb2\xb3\xe5\x8c\x97 \xe6\xb2\xb3\xe5\x8d\x97'

# 和 StringIO类似 可以用一个bytes初始化 BytesIO

t = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(t.read())  # b'\xe4\xb8\xad\xe6\x96\x87'

'''StringIO和BytesIO 是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口'''







































