import wx
import random

class GamePanel(wx.Panel):

    def __init__(self, parent, size):
        wx.Panel.__init__(self, parent, size=size)
        self._values= [i for i in range(16)]
        self._shuffle()
        wx.CallLater(1000, self._drawTiles)
        self.Bind(wx.EVT_KEY_UP, self._handleKeyDown)

    def _shuffle(self):
        for i in range(20):
            success = False
            while not success:
                direction = random.randint(1, 4)
                if 1 == direction:
                    success = self._moveHoleLeft()
                elif 2 == direction:
                    success = self._moveHoleRight()
                elif 3 == direction:
                    success = self._moveHoleUp()
                elif 4 == direction:
                    success = self._moveHoleDown()


    def _findHoleIndex(self):
        position = -1
        for index in range(len(self._values)):
            current_value = self._values[index]
            if 0 == current_value:
                position = index
        return position 

    def _swapValues(self, index1, index2):
        temp = self._values[index1]
        self._values[index1] = self._values[index2]
        self._values[index2] = temp

    def _handleKeyDown(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_UP:
            self._moveHoleUp()
            self._drawTiles()
            event.Skip()
        elif key == wx.WXK_DOWN:
            self._moveHoleDown()
            self._drawTiles()
            event.Skip()
        elif key == wx.WXK_LEFT:
            self._moveHoleLeft()
            self._drawTiles()
            event.Skip()
        elif key == wx.WXK_RIGHT:
            self._moveHoleRight()
            self._drawTiles()
            event.Skip()

    def _moveHoleUp(self):
        hole_index = self._findHoleIndex()
        if hole_index > 3:
            self._swapValues(hole_index, hole_index-4)
            return True
        return False

    def _moveHoleDown(self):
        hole_index = self._findHoleIndex()
        if hole_index < 12:
            self._swapValues(hole_index, hole_index+4)
            return True
        return False

    def _moveHoleLeft(self):
        hole_index = self._findHoleIndex()
        if hole_index % 4 > 0:
            self._swapValues(hole_index, hole_index-1)
            return True
        return False

    def _moveHoleRight(self):
        hole_index = self._findHoleIndex()
        if hole_index % 4 < 3:
            self._swapValues(hole_index, hole_index+1)
            return True
        return False

    def _drawTiles(self):
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
