import wx

class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self)
        self.Create(None, title="Sliding puzzle", size=(400, 500))
        self.Center()
        self._values= [i for i in range(16)]
        wx.CallLater(1000, self.DrawTiles)

    def DrawTiles(self):
        dc = wx.ClientDC(self)
        pen = wx.Pen(wx.BLACK)
        pen.SetWidth(10)
        font = wx.Font()
        font.SetPointSize(32)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        dc.SetPen(pen)
        dc.SetFont(font)

        for row in range(4):
            for col in range(4):
                value = self._values[col + 4*row]
                dc.DrawLine(20 + 80*col, 20 + 80*row, 100 + 80*col, 20 + 80*row)
                dc.DrawLine(100 + 80*col, 20 + 80*row, 100 + 80*col, 100 + 80*row)
                dc.DrawLine(100 + 80*col, 100 + 80*row, 20 + 80*col, 100 + 80*row)
                dc.DrawLine(20 + 80*col, 100 + 80*row, 20 + 80*col, 20 + 80*row)
                dc.SetBrush(wx.Brush('#cde' if value > 0 else wx.RED))
                dc.DrawRectangle(20 + 80*col, 20 + 80*row, 80, 80)
                if value > 0:
                    dc.DrawText(str(value), 30 + 80 * col, 30 + 80 * row)
