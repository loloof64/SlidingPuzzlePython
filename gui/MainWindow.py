import wx

class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self)
        self.Create(None, title="Sliding puzzle", size=(600,700))
