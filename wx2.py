# -*- coding:  utf-8  -*-
# ------------------------------

#创建 实验楼 窗口
import webbrowser
import wx
import time

#事件
def searchevent(event):
	webbrowser.open('http://www.baidu.com')

def quitevent(event):
	wx.Exit()

def openfile(event):
	f = open(filename.GetValue())
	contents.SetValue(f.read())
	f.close()

def writefile(event):
	f = open(filename.GetValue(), 'w')
	f.write(contents.GetValue())
	f.close()

def times(event):
	t= time.time()
	t1=time.localtime(t)
	t2=time.asctime(t1)
	print(t2)


app = wx.App()
win = wx.Frame(None, title="实验楼", pos=(200,300),size=(666,555))#创建窗口

panel = wx.Panel(win)#创建背景组件

openB = wx.Button(panel,label="Open")# 创建按钮
writeB = wx.Button(panel, label="Write")
traintimeB = wx.Button(panel, label="Traintime")
memberB = wx.Button(panel, label="Member")
searchB = wx.Button(panel, label="Search")
quitB = wx.Button(panel, label='Quit')

#窗口控件

#filename = wx.TextCtrl(panel,style = wx.TE_MULTILINE | wx.HSCROLL)
filename = wx.TextCtrl(panel)
contents = wx.TextCtrl(panel, style = wx.TE_MULTILINE | wx.HSCROLL)
#memberB = wx.TextAttr(colText, colBack=wx.NullColor, font=wx.NullFont)

#BoxSizer尺寸器

hbox = wx.BoxSizer() #默认水平
#gbox = wx.GridSizer()
#ggbox = wx.GridBagSizer()
#wbox = wx.StaticBoxSizer()

hbox.Add(filename, proportion=2,flag=wx.EXPAND)
#hbox.Add(contents, proportion=1, flag=wx.LEFT)

hbox.Add(openB, proportion=1, flag=wx.LEFT, border=5)
hbox.Add(writeB, proportion=1,flag=wx.LEFT, border=5)
hbox.Add(traintimeB, proportion=1, flag=wx.LEFT, border=5)
hbox.Add(memberB, proportion=1, flag=wx.LEFT, border=5)
hbox.Add(searchB, proportion=1, flag=wx.LEFT, border=5)
hbox.Add(quitB, proportion=1)

vbox = wx.BoxSizer(wx.VERTICAL)#垂直

vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND,border=5)

#事件
searchB.Bind(wx.EVT_BUTTON, searchevent)
quitB.Bind(wx.EVT_BUTTON, quitevent)
openB.Bind(wx.EVT_BUTTON, openfile)
writeB.Bind(wx.EVT_BUTTON, writefile)
traintimeB.Bind(wx.EVT_BUTTON,times)

panel.SetSizer(vbox)

win.Show()
app.MainLoop()


print('------------------------------------------')

import wx

class MyFrame(wx.Frame):


	def __init__(self):
		wx.Frame.__init__(self,None,-1,title='Hello wxPython World', size=(400,300))
		panel = wx.Panel(self,-1)
		
		self.hello = wx.Button(panel,-1,label='python')
		self.python = wx.Button(panel,-1,label='world')
		
		self.filename = wx.TextCtrl(panel,-1)
		self.content = wx.TextCtrl(panel,-1, style=wx.TE_MULTILINE | wx.HSCROLL)
		
		self.hello.Bind(wx.EVT_BUTTON, self.ev1)
		self.python.Bind(wx.EVT_BUTTON,self.ev2)
		
		self.hbox = wx.BoxSizer()
		self.hbox.Add(self.filename, proportion=1, flag=wx.EXPAND)
		self.hbox.Add(self.hello, proportion=1, flag=wx.RIGHT, border=5)
		self.hbox.Add(self.python, proportion=1, flag=wx.LEFT, border=5)
		#self.hbox.Add(self.filename, proportion=1, flag=wx.EXPAND) #窗口按钮排列与先后顺序有关
	
		self.vbox = wx.BoxSizer(wx.VERTICAL)
		self.vbox.Add(self.hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
		self.vbox.Add(self.content, proportion=1, flag=wx.EXPAND | wx.ALL | wx.BOTTOM | wx.RIGHT
						| wx.TOP, border=5)

		panel.SetSizer(self.vbox)
	def ev1(self,event):
		print('Hello python world')
	def ev2(self,event):
		self.Destroy()

		


if __name__ == '__main__':
	app = wx.PySimpleApp()
	MyFrame().Show()
	app.MainLoop()




















