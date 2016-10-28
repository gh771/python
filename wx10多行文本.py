# -*- coding:  utf-8  -*-
# ------------------------------

# 创建多行文本

import wx

class TextFrame(wx.Frame):
	
	def __init__(self):
		wx.Frame.__init__(self,parent=None,id=-1,title='Text Entry Example',
					size=(700,500))
		panel = wx.Panel(self,-1)
		multiLabel = wx.StaticText(panel,-1,"Multi-line")
		multiText = wx.TextCtrl(panel,-1,
			"Here is a loooooong line of test set in the control.\n\n"
			"See that it wrapped, and that this line is after blank",
			size=(300,200), style=wx.TE_MULTILINE | wx.TE_RICH) #创建一个文本控件
		multiText.SetInsertionPoint(0) #设置插入点

		richLabel = wx.StaticText(panel,-1,"Rich Text")
		richText = wx.TextCtrl(panel,-1,
			"If supported by the native control, this is reveresd, and  this\
			 is a different font.",
			size=(300,200), style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.HSCROLL)#创建丰富文本控件
		richText.SetInsertionPoint(0)
		richText.SetStyle(44,52,wx.TextAttr('white', 'black'))#设置文本样式
		points = richText.GetFont().GetPointSize()
		f = wx.Font(points +3, wx.ROMAN, wx.ITALIC, wx.BOLD, True) #创建一个字体
		richText.SetStyle(68,82,wx.TextAttr("blue", wx.NullColour,f)) #用新字设置样式
		
		sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
		sizer.AddMany([multiLabel, multiText, richLabel, richText])
		panel.SetSizer(sizer)

if __name__ =='__main__':
	app = wx.PySimpleApp()
	frame = TextFrame()
	frame.Show()
	app.MainLoop()







