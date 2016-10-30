# -*- coding:  utf-8  -*-
# ------------------------------

'''窗口内鼠标移动POS框显示鼠标位置'''

import wx

# 创建一个App

class App(wx.App):
	def __init__(self):
		super(self.__class__, self).__init__() #如果要重写 __init__, 必须调用wx.App的 __init__，
							#否则OnInit方法不会被调用
	def OnInit(self):
		frame = MyFrame() #通常在这个方法里对程序进行初始化， 如创建并显示frame
		frame.Show(True)
		self.SetTopWindow(frame) # 设置顶级窗口，将此 frame设置为顶级窗口
		return True     #这里必须return True， 表示正确初始化，否则程序将终止


class MyFrame(wx.Frame):
	def __init__(self): #初始化父类，指定窗口基本属性
		super(self.__class__, self).__init__(parent=None, id=-1, title ='My Frame', size=(300,300))
		panel = wx.Panel(parent = self, id = -1) #定义一个Panel
		panel.Bind(wx.EVT_MOTION, self.OnMove)  #绑定 MOTION事件
		wx.StaticText(parent = panel, id = -1, label = 'Pos:', pos = (10,12)) # 创建一个label: StaticText
		self.posCtrl = wx.TextCtrl(parent = panel, id = -1, value = '', pos = (40,10)) #创建一个文本框:TextCtrl

	def OnMove(self, event):
		pos = event.GetPosition()
		self.posCtrl.SetValue('%s, %s' %(pos.x,pos.y))

if __name__ == '__main__':
#程序必须有一个wx.App来开始程序
	app = App()
	app.MainLoop()









