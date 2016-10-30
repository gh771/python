# -*- coding:  utf-8  -*-
# ------------------------------
'''
print('-----------------------通用按钮---------------------------')
# 通用按钮是一个完全用python重新实现的一个按钮窗口部件，回避了本地系统窗口的部件的用法
# 它的父类是 wx.lib.buttons.GenButton 通用按钮有通用位图和切换按钮
# 控件wx.FlexGridSizer(rows=1,cols=0,vgap=0,hgap=0)
# rows定义 GridSizer行数， cols定义GridSizer列数， vgap定义垂直方向上行间距，hgap定义水平方向上列间距

import wx
import wx.lib.buttons as buttons

class GenericButtonFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Generic Button Example',size=(620,400))#原例(500,350)
		panel = wx.Panel(self,-1)

		sizer = wx.FlexGridSizer(4,3,15,5)#原例(1,3,20,20) #网格粒度
		b = wx.Button(panel, -1, "A wx.Button")
		b.SetDefault()
		sizer.Add(b)
		
		b = wx.Button(panel,-1, "non-default wx.Button")
		sizer.Add(b)
		sizer.Add((10,10))
		
		b = buttons.GenButton(panel,-1, "Generic Button") #基本的通用按钮
		sizer.Add(b)

		b = buttons.GenButton(panel,-1, "disabled Genreic") # 无效的通用按钮
		b.Enable(False)
		sizer.Add(b)

		b = buttons.GenButton(panel, -1, "bigger") #自定义尺寸和颜色的按钮
		b.SetFont(wx.Font(20,wx.SWISS, wx.NORMAL, wx.BOLD, False))
		b.SetBezelWidth(5)
		b.SetBackgroundColour('brown')
		b.SetForegroundColour('black')
		b.SetToolTipString('This is BIG button....')
		sizer.Add(b)

		bmp = wx.Image('wxpython1.jpg', wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
		b = buttons.GenBitmapButton(panel,-1,bmp) #通用位图按钮
		sizer.Add(b)
	
		b = buttons.GenBitmapToggleButton(panel,-1,bmp) #通用位图开关按钮
		sizer.Add(b)

		b = buttons.GenBitmapTextButton(panel,-1,bmp,"Bitmapped Text",
						size=(270,75)) #位图文本按钮原例(175,75)
		b.SetUseFocusIndicator(False)
		sizer.Add(b)
	
		b = buttons.GenToggleButton(panel,-1, "Toggle Button") #通用开关按钮
		sizer.Add(b)
		
		panel.SetSizer(sizer)

if __name__ == '__main__':
	app = wx.App()
	frame = GenericButtonFrame()
	frame.Show()
	app.MainLoop()

'''
print('-----------------------------滑块-----------------------------------')

# -*- coding:  utf-8  -*-
# ------------------------------
# wxpython中用于输入数字和显示的工具 滑块(slider) 微调控制框和显示量度的标尺
#滑块是一个窗口部件通过在该控件的尺度内拖动指示器来选择一个数值
#在wxpython中该控件类是wx.Slider
#wx.Slider(parent, id,value,minValue,maxValue,pos=(wxDefaultPosition)
#size=(wx.DefaultSizer, style=wx.SL_HORIZONTAL,validator=wx.DefaultValidator,name='slider')
#value是滑块初始值， minValue和maxValue是两端的值

#水平和垂直滑块

import wx	

class SliderFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'Slider Example',size=(300,350))#父类构造器
		panel = wx.Panel(self,-1)#背景组件 控件容器
		self.count = 0
		slider = wx.Slider(panel,100,20,1,150,pos=(10,10),size=(250,-1),
				style=wx.SL_HORIZONTAL |wx.SL_AUTOTICKS | wx.SL_LABELS)
		slider.SetTickFreq(5,1)
		slider = wx.Slider(parent=panel,id=100,value=25,minValue=1,maxValue=100,pos=(105,70),size=(-1,250),
				style=wx.SL_VERTICAL | wx.SL_AUTOTICKS |wx.SL_LABELS )
		slider.SetTickFreq(5,1)


# style= wx.SL_AUTOTICKS(显示滑块刻度，刻度间隔通过SetTicks方法控制)， wx.SL_HORIZONTAL(水平滑块默认值)
#wx.SL_VERTICAL(垂直滑块) wx.SL_LABELS(滑块显示两头的值和滑块的当前只读值)


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = SliderFrame()
	frame.Show()
	app.MainLoop()














		
