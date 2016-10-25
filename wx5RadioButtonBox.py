# -*- coding:  utf-8  -*-
# ------------------------------



'''
print('----------------------------单选按钮--------------------------------')
# 单选按钮是一种允许用户从几个选项中选择其一的窗口部件
# 创建单选按钮(radio button) #wxpython中有两种方法创建单选按钮 1wx.RadioButton 它要求一次创建一个按钮
# 而 wx.RadioBox 使你可以用单一对象来配置完整的一组按钮 这些按钮显示在一个矩形中

# wx.RadioButton(parent,id,label,pos=wx.DefaultPostion,size=wx.DefaultSize,style=0,
#		validator=wx.DefaultValidator,name='radioButton')
# wx.RB_GROUP样式声明该按钮位于一组单选按钮开头 一组单选按钮的定义控制着开关行为，当组中一个annie被
#选中时 先前被选中的按钮被切换到未选中状态

import wx


class RadioButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Radio Button',size=(200,200))
		panel = wx.Panel(self,-1)
		
	#创建单选按钮                         #wx.RB_GROUP样式声明该按钮位于一组单选按钮开头
		radio1 = wx.RadioButton(panel,-1,'Elmo',pos=(20,50),style=wx.RB_GROUP)
		radio2 = wx.RadioButton(panel,-1,'Ernie',pos=(20,80))
		radio3 = wx.RadioButton(panel,-1,'Bert',pos=(20,110))

	#创建文本控件
		text1 = wx.TextCtrl(panel,-1,'',pos=(80,50))
		text2 = wx.TextCtrl(panel,-1,'',pos=(80,80))
		text3 = wx.TextCtrl(panel,-1,'',pos=(80,110))
		self.texts = {"Elmo": text1, "Ernie":text2, "Bert":text3} #连接按钮和文本
		for eachText in [text2,text3]:
			eachText.Enable(False)#初始值两个事件设为False，使得两个文本框无效
		for eachRadio in [radio1, radio2, radio3]: #按钮循环绑定事件
			self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio,eachRadio)
		self.selectedText = text1
	
	def OnRadio(self,event): #事件处理
		if self.selectedText:#点击其他事件时事件1被设为False
			self.selectedText.Enable(False)
		radioSelected = event.GetEventObject()
		text = self.texts[radioSelected.GetLabel()]
		text.Enable(True) #获取事件对象后，获取事件对象标签，在字典里获取标签对应事件，使值为True
		self.selectedText = text # 点击当前按钮后其他按钮文本框被设为False

if __name__ =='__main__':
	app = wx.PySimpleApp()
	RadioButtonFrame().Show()
	app.MainLoop()
'''


print('-----------------------------------单选框---------------------------')
#使用单选框 wx.RadioBox
#RadioBox类让你能够创建一个单一的对象，该对象包含了完整的组
# wx.RadioBox(parent,id,label,pos=wx.DefaultPostion,size-wx.DefaultSize,
# choices=None, majorDimension=0,style=wx.RA_SPECIFY_COLS, validator=wx.DEfaultValidator,
#name="radioBox')


import wx

class RadioBoxFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Radio Box Example',size=(350,200))
		panel = wx.Panel(self,-1)
		sampleList = ['zero','one','two','three','four','five','xis','seven','eight']
		
		wx.RadioBox(panel,-1,'A Radio Box',(10,10),wx.DefaultSize,sampleList,2,
				wx.RA_SPECIFY_COLS)
		
		wx.RadioBox(parent=panel,id=-1,label='',pos=(150,10),size=wx.DefaultSize,
                    choices=sampleList,majorDimension=3,
                    style=wx.RA_SPECIFY_COLS | wx.NO_BORDER)

if __name__ =='__main__':
	app = wx.PySimpleApp()
	RadioBoxFrame().Show()
	app.MainLoop()

#这些按钮使用choices参数指定 它是一个python的字符串标签的序列
#如同网格一样使用维数的尺寸来之定wx.RadioBox的尺度,维度的主尺寸使用major Dimension参数指定
#默认值是 wx.RA_SPECIFY_COLS， 本例左框列数设为2,右侧为3,行数由choices列表元素动态决定
# style 设置为wx.RA_SPECIFY_ROWS得到相反的行为，
#使用 wx.EVT_RADIOBOX 响应命令事件




















