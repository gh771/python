#/usr/bin/python
# -*- coding:  utf-8  -*-
# ------------------------------

'''  # wx 包中的方法都是以大写字母开头的，原因是这些方法名和基础的 C++包 wxWidgets中的方法名都是对应的
     #窗口也成为框架(Frame),它是 wx.Frame的实例。wx 框架中的部件都是由它的父部件使用 构造函数的第一参数创建的
      wx.Window 是一个基类许多构建从它继承，包括 wx.Frame构件 可以在所有的子类中使用 wx.Window方法
# wx.python的几种方法
 SetTitle(string title) ---设置窗口标题，只可用于框架和对话框
	SetToolTip(wx.ToolTip tip) ---为窗口添加提示
	SetSize(wx.Size size) --- 设置窗口尺寸
	SetPosition(wx.Point pos) ---设置窗口出现的位置
	Show(show=True) --- 显示或隐藏窗口 参数可为 True或 False
	Move(wx.Point pos) --- 将窗口移动到指定位置
	SetCursur(wx.StockCursur id) --- 设置窗口的鼠标指针样式
'''


import wx 

app = wx.App() #如果wx.App无法工作，可能需要将它替换为wx.PySimpleApp
''' 实用的方法是为 wx构造函数使用关键字参数，不用记住参数的顺序'''
win = wx.Frame(None, title = "Simple Editor", size=(410,335))# 在创建部件的时候使用 title参数设定框架的标题
					#使用 pos 和 size参数在构造函数内设置按钮位置和尺寸
loadButton = wx.Button(win, label = 'Open', pos=(225,5),size=(80,25)) # 在创建部件的时候使用构造函数的 label参数设定它们的标签

saveButton = wx.Button(win, label = 'Save', pos=(315,5), size=(80,25))

filename = wx.TextCtrl(win, pos=(5,5), size=(210,25))# 创建两个文本控件(text control)两个(wx.TextCtrl对象)

contents = wx.TextCtrl(win, pos=(5,35), size=(390,260), style= wx.TE_MULTILINE or wx.HSCROLL)
	#创建文本区(text area)使用style参数调整风格 #style参数的值实际上是个整数但不用直接指定，
	#可以使用按位或(或者管道运算符)联合 wx模块中具有特殊名字的风格来指定，
	#这里使用 wx.TE_MULTILINE来获取多行文本区，wx.HSCROLL获取水平滚动条1.py

##btn = wx.Button(win) # 在框架上增加按钮 只要使用 win 作为父参数实例化 wx.Button

win.Show()# 在调用 app.MainLoop()前需要调用窗口的Show方法 否则它会一直隐藏
		#事件是每一个GUI应用程序的组成部分，所有的GUI应用程序是事件驱动的

app.MainLoop()


