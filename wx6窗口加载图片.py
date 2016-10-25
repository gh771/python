# -*- coding:  utf-8  -*-
# ------------------------------


# No such file or directory
# Failed to load image from file 'th5.jpg'
# 图片 示例 窗口加载一张图片
import wx


class Frame(wx.Frame):  # wxPrame subcclass """Frame class that display a image"""

	def __init__(self, image, parent=None, id=-1,
				 pos=wx.DefaultPosition,
				 title="Hello, wxpython"):  # 3 #create a Frame instance and display a image
		temp = image.ConvertToBitmap()
		size = temp.GetWidth(), temp.GetHeight()
		wx.Frame.__init__(self, parent, id, title, pos, size)
		self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
		pass


class App(wx.App):  # 5 #wx.App subclass
	"""Application class"""

	def OnInit(self):
		image = wx.Image('wxpython.jpg', wx.BITMAP_TYPE_JPEG)
		self.frame = Frame(image)

		self.frame.Show(True)
		self.SetTopWindow(self.frame)
		return True


def main():
	app = App()
	app.MainLoop()


if __name__ == '__main__':
	main()
