import wx

from gui.GamePanel import GamePanel

class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self)
        self.Create(None, title="Sliding puzzle", size=(400, 420))
        self._panel = GamePanel(self, size=(400,400))
        self._panel.Show()
        self.Center()
        