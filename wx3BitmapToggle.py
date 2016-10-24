# -*- coding:  utf-8  -*-
# ------------------------------

'''
import wx
print('-------------------------简单按钮示例----------------------------------')

class Buttonframe(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None, id=-1, title='BUTTON EXAMPLE',size=(333,222))
		panel = wx.Panel(self,-1)
		self.button = wx.Button(panel, -1,label='Hello', pos=(1,5))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
		self.button.SetDefault()#设置按钮为对话框或框架的默认按钮,默认按钮的绘制不同于其他按钮
					#它在对话框获得焦点时，通常按下回车键被激活
		#print(self.GetDefaultSize())
	
	def OnClick(self, enent):
		self.button.SetLabel("Clicked")# 按钮文本使用SetLabel()来改变
		#self.button.SetLabel('Examination')
		#print(self.button.GetLabel()) # 使用 GetLabel()来获取按钮文本
		print(self.GetDefaultSize()) #放在事件函数中每次点击按钮都返回尺寸
		#GetDefaultsize() 返回系统默认按钮的尺寸(对于框架间的一致性时用用的)

# wx.Button类有一个跨平台的样式标记 wx.BU_EXACTFIT 如果定义了这个标记，那么按钮就不把系统默认的尺寸作为最小的尺寸
# 而是把能够恰好填充标签的尺寸作为最小尺寸

if __name__ == '__main__':
	app = wx.App()
	frame = Buttonframe()
	frame.Show()
	app.MainLoop()

print('----------------------------------生成图一个位图按钮----------------------------------------')

#使用类 wx.BitmapButton来创建一个位图按钮


import wx
class BitmapButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None,-1,'Bitmap Button Example',size=(400,300))
		panel = wx.Panel(self,-1)
		bmp = wx.Image("wxpython1.jpg",wx.BITMAP_TYPE_JPEG).ConvertToBitmap()#原例BMP格式
		self.button = wx.BitmapButton(panel, -1, bmp, pos=(10,20))
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
		self.button.SetDefault()
		self.button2 = wx.BitmapButton(panel,-1,bmp,pos=(200,20),style=12)
		self.Bind(wx.EVT_BUTTON, self.OnClick, self.button2)
		
	def OnClick(self,event):
		self.Destroy()# Destroy参数 点击图片窗口关闭


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = BitmapButtonFrame()
	frame.Show()
	app.MainLoop()

'''

print('--------------------------创建开关按钮--------------------------------')


# -*- coding:  utf-8  -*-
# ------------------------------

#使用 wx.ToggleButton创建一个开关按钮
#开关按钮(toggle button) 看起来十分像文本按钮，但它的行为更像复选框，它的选择或非选择状态时可视化的
#换句化说当你按下一个开关按钮(toggle button)时，它将一致保持被按下的状态直到你再次敲击它
#与父类wx.Button 之间只有两个区别， 当被敲击时wx.ToggleButton发送一个EVT_TOGGLEBUTTON事件
# wx.ToggleButton 有 GetValue() 和 SetValue()方法，它们处理按钮的二进制状态

import wx

class ToggleButtonFrame(wx.Frame):

	def __init__(self):
		wx.Frame.__init__(self,None,-1,title='Toggle Button', size=(200,150))
		panel = wx.Panel(self,-1)
		self.button = wx.ToggleButton(panel,label='test', pos=(10,20),size=(100,30))
		self.button1 = wx.ToggleButton(panel,label='test1',pos=(20,50),size=(100,30))
		
		self.Bind(wx.EVT_TOGGLEBUTTON, self.event, self.button)
		self.Bind(wx.EVT_TOGGLEBUTTON, self.event1, self.button1)
		print(self.button1.GetValue())

	def event(self,event):
		self. Destroy()

	def event1(self,event):
		print('self.Destroy')
		print(self.button1.GetValue())# True or False
		self.button.SetValue(False)

if __name__ == '__main__':
	app = wx.App()
	fram = ToggleButtonFrame()
	fram.Show()
	app.MainLoop()

 










