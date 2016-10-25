# -*- coding:  utf-8  -*-
# ------------------------------

# 简单的文本编辑器示例

import wx

#事件函数
def load(event):
	file = open(filename.GetValue())#GetValue获取文件名
	contents.SetValue(file.read())# SetValue将文本引入文本区
	file.close()

def save(event):
	file = open(filename.GetValue(), 'w')
	file.write(contents.GetValue())
	file.close()

app = wx.App()#必须创建的应用程序对象，它负责幕后所有的初始化，如果wx.App无法工作，替换为wx.PySimpleApp
win = wx.Frame(None, title='Simple Editor', size=(410,335))#创建框架wx.Frame类实例# wx框架中的部件由它的父部件使用构造函数的第一个参数创建的，如果创建一个单独的窗口就不需要考虑父部件，使用None即可
bkg = wx.Panel(win)#背景组件 

loadButton = wx.Button(bkg, label='Open')# 按钮
loadButton.Bind(wx.EVT_BUTTON, load) #绑定事件

saveButton = wx.Button(bkg, label='Save')
saveButton.Bind(wx.EVT_BUTTON, save)#当事件处理函数被调用时，它会收到一个事件对象作为它唯一的参数

filename = wx.TextCtrl(bkg)#文本控件
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)#style参数调整控件风格

hbox = wx.BoxSizer()# 尺寸器 #wx.HORIZONTAL wx.VERTICAL 参数决定水平或垂直，默认水平
hbox.Add(filename, proportion=1, flag=wx.EXPAND)#Add方法proportion参数根据窗口改变大小时分配空间比例
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)#flag参数

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)# border边框参数 设置边缘宽度
vbox.Add(contents, proportion=1,
		flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
		# flag参数使用or或|连接构造符号常量(symbolic constant即有特殊名字的整数)对其进行构造
		#wx.EXPAND标记确保组件会扩展到所分配的空间中，wx.LEFT wx.RIGHT wx.TOP wx.BOTTOM wx.ALL
		#标记决定边框参数应用于哪个边

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()
#在调用app.MainLoop()方法前需要调用Show方法，否则窗口会隐藏




