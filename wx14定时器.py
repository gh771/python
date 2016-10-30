# -*- coding:  utf-8  -*-
# ------------------------------


# 介绍 wxpython定时器 wx.Timer简单应用
# python 使用 wxpython创建窗口应用程序以及定时器的相关使用

import wx
import time


class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u'测试定时器的小程序',
                          pos=wx.DefaultPosition, size=wx.Size(483, 155),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(
            wx.SYS_COLOUR_INACTIVECAPTIONTEXT))

        gSizer1 = wx.GridSizer(0, 2, 0, 0)
        self.m_btnStart = wx.Button(self, wx.ID_ANY, u'启动定时器',
                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_btnStart, 0, wx.ALL, 5)

        self.m_btnStop = wx.Button(self, wx.ID_ANY, u'停止定时器',
                                   wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_btnStop, 0, wx.ALL, 5)

        self.SetSizer(gSizer1)
        self.Layout()
        self.m_startusBar1 = self.CreateStatusBar(2, wx.ST_SIZEGRIP, wx.ID_ANY)
        self.Centre(wx.BOTH)

        # Connect Events
        self.m_btnStart.Bind(wx.EVT_BUTTON, self.OnStart)
        self.m_btnStop.Bind(wx.EVT_BUTTON, self.OnStop)
        # 创建定时器
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)  # 绑定定时器事件
        StrYMDt = time.strftime("%Y-%B-%d")
        self.SetStatusText(StrYMDt, 0)  # 显示年月日
        StrIMSt = time.strftime("%I: %M: %S")
        self.SetStatusText(StrIMSt, 1)  # 显示时间

    def __del__(self):
        pass  # Virtual event handlers, overide them in your derived class#虚拟语柄覆盖派生类

    def OnStart(self, event):
        self.timer.Start(10)  # 设定时间间隔为1000毫秒，并启动定时器

    def OnStop(self, event):
        self.timer.Stop()

    def OnTimer(self, evt):  # 显示时间事件处理函数
        t = time.localtime(time.time())


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()


