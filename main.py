import wx
from gui.MainWindow import MainWindow

class SlidingPuzzle(wx.App):

    def OnInit(self):
        self.SetAppName("Sliding Puzzle")
        return True

if __name__ == '__main__':
    app = SlidingPuzzle()
    mainWindow = MainWindow()
    mainWindow.Show()
    app.MainLoop()