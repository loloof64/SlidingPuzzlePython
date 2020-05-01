import wx

from gui.MainPanel import MainPanel

class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self)
        self.Create(None, title="Sliding puzzle", size=(400, 500))
        self._panel = MainPanel(self, size=(400,400))
        self._panel.Show()
        self.Center()
        