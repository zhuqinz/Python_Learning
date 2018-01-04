import wx
 
########################################################################
class Car(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, make, model, year, color="Blue"):
        """Constructor"""
        self.id = id(self)
        self.make = make
        self.model = model
        self.year = year
        self.color = color
 
 
########################################################################
class MyPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
 
        rows = [Car("Ford", "Taurus", "1996"),
                Car("Nissan", "370Z", "2010"),
                Car("Porche", "911", "2009", "Red")
                ]
 
        self.list_ctrl = wx.ListCtrl(self, size=(-1,100),
                                style=wx.LC_REPORT
                                |wx.BORDER_SUNKEN
                                )
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onItemSelected)
        self.list_ctrl.InsertColumn(0, "Make")
        self.list_ctrl.InsertColumn(1, "Model")
        self.list_ctrl.InsertColumn(2, "Year")
        self.list_ctrl.InsertColumn(3, "Color")
 
        index = 0
        self.myRowDict = {}
        for row in rows:
            self.list_ctrl.InsertStringItem(index, row.make)
            self.list_ctrl.SetStringItem(index, 1, row.model)
            self.list_ctrl.SetStringItem(index, 2, row.year)
            self.list_ctrl.SetStringItem(index, 3, row.color)
            self.list_ctrl.SetItemData(index, row.id)
            if index % 2:
                self.list_ctrl.SetItemBackgroundColour(index, "white")
            else:
                self.list_ctrl.SetItemBackgroundColour(index, "yellow")
            self.myRowDict[row.id] = row
            index += 1
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onItemSelected(self, event):
        """"""
        currentItem = event.m_itemIndex
        car = self.myRowDict[self.list_ctrl.GetItemData(currentItem)]
        print car.make
        print car.model
        print car.color
        print car.year
 
########################################################################
class MyFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "List Control Tutorial")
        panel = MyPanel(self)
        self.Show()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()