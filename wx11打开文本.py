# -*- coding:  utf-8  -*-
# ------------------------------

#打开文本例子

import wx 

class MyFrame(wx.Frame):
	def __init__(self,parent, id, title,data):
		wx.Frame.__init__(self,parent, id, title, wx.DefaultPosition,size=(500,380))

		panel = wx.Panel(self,-1)
		
		# font type: wx.DEFAULT, wx.DECORATIVE, wx.ROMAN, wx.SCRIPT, wx.SWISS, wx.MODERN

		#slant: wx.NORMAL, wx.SLANT or wx.ITALIC
		#weight: wx.NORMAL, wx.LIGHT or wx.BOLD
		# font1 = wx.Font(10, wx.SWISS, wx.ITALIC, wx.NORMAL)
		# use additiona; fonts this way

		font1 = wx.Font(10, wx.SWISS, wx.NORMAL,wx.NORMAL, False, u'Comic Sans MS')
	
		test1 = wx.StaticText(panel, -1, data, pos=(20,15))
		test1.SetFont(font1)
		# center frame on screen
		self.Center()
		# show the frame
		self.Show(True)
	

data = """\
Al Gore: The Wild Years
America's Most Popular Lawyers
Career Opportunities for History Majors
Different Ways to Spell 'Bob'
Dr.Kevorkian's Collection of Motivational Speeches
Ethiopian Tips on World Dominanice
Everything Men Know About Women
Everything Women Know About Men
One Hundred and One Spotted Owl Recipes by the EPA
Staple Your Way to Success
The Amish Phone Book
The Engineer's Guide to Fashion
Ralph Nader's list of pleasurs"""

application = wx.PySimpleApp()
#Create instance of calss MyFrame
window = MyFrame(None, -1, "The World's Shortest Books", data)
# start the event loop
application.MainLoop()





