# -*- coding:  utf-8  -*-
#-----------------------------------------------

#Tkinter 

'''
#添加不同颜色的Frame大小均为20*400
from tkinter import *


def hello():
	print('Hello world')

win = Tk()
for fm in ['red','blue','yellow','green','white','black']:
	Frame(height=20, width=400,bg=fm).pack()
win.mainloop()
 
 
print('--------------------------------------------------------')
#向Frame中添加Widget
root = Tk()
fm=[]
for color in ['blue','red','brown']:
	fm.append(Frame(height=200,width=400,bg=color))

Label(fm[1],text='Hello label').pack()
fm[0].pack()
fm[1].pack()
root.mainloop()


#title
rook =Tk()

for lf in ['red','blue','yellow']:
	LabelFrame(height=200,width=300,text=lf,bg=lf).pack()

rook.mainloop()
'''
print('-----------------------------------------------------------')

from tkinter import *
'''
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	
	def createWidgets(self):
		self.helloLabel = Label(self, text = "Hello, world")
		self.helloLabel.pack()
		self.quitButton = Button(self, text='Quit', command = self.quit)
		self.quitButton.pack()

app = Application()

app.master.title('Hello World')

app.mainloop()

'''
print('-------------------------------------------------------------')

import tkinter.messagebox as messagebox

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alerButton = Button(self, text='Hello', command = self.hello)
		self.alerButton.pack()
	
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()

app.master.title('Hello World')

app.mainloop()






