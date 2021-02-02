import wx,time

app = wx.App()

frame = wx.Frame(None, -1, 'My First GUI in Python')
frame.Centre()
a=(500,50)
frame.SetSize(a)
frame.Show()
for i in range(500):
    frame.MoveXY(i,i)
    time.sleep(0.01)

app.MainLoop()




           ( )
            |
        ____|____
            |
           / \
          /   \
