# -*- coding:  utf-8  -*-
# ------------------------------

'''
# 在wxpython中，类wx.SpinCtrl 管理微调按钮和相应的文本显示


import wx

class SpinnerFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Spinner Example',size=(200,100))
		panel = wx.Panel(self,-1)
		sc = wx.SpinCtrl(panel,-1,'',(30,20),(80,-1))
		sc.SetRange(1,100)#范围
		sc.SetValue(1)#初始值

if __name__ == '__main__':
	app = wx.PySimpleApp()
	SpinnerFrame().Show()
	app.MainLoop()

#微调控件所有复杂的东西都是在其构造函数中
# wx.SpinnerCtrl(parent,id=-1,value=wx.EmptyString,pos=wx.DefaultPosition,size=wx.DefaultSize,
#		style=wx.SP_ARROW_KEYS,min=0,max=100,initial=0,name='wxSpinCtrl')

'''
#进度条 # wxpython窗口部件 wx.Gauge

# wx.Gauge(parent,id,range,pos=wx.DefaultPosition,size=wx.DefaultSize,style=wx.GA_HORIZONTAL,
#		validtor=wx.DefaultValidator,name="gauge")
#参数range指定数字值时该值代表标尺的上限，下限总是0 #
#默认样式wx.GA_HORIZONTAL提供一个水平条，使用wx.GA_VERTICAL 将它旋转90度
#

import wx

class GaugeFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"Gauge Example",size=(350,150))
		panel = wx.Panel(self,-1)
		self.count = 0
		self.gauge = wx.Gauge(panel,-1,500,(20,50),(250,25))#,style=wx.GA_VERTICAL)
		self.gauge.SetBezelFace(3)
		self.gauge.SetShadowWidth(3)
		self.Bind(wx.EVT_IDLE, self.OnIdle)

	def OnIdle(self,event):
		self.count = self.count +1
		if self.count == 500:
			self.count = 0
		self.gauge.SetValue(self.count)

#wx.Gauge作为一个只读控件没有事件，但它的属性可以设置，使用GetValue(),Set-Value(pos),GetRange()
# 和SetRange(range) 来调整它的值和范围


if __name__ == '__main__':
	app = wx.PySimpleApp()
	GaugeFrame().Show()
	app.MainLoop()



















