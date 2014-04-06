import wx
import PeruConstants, PersonUI, SourceUI, MatrixUI

def GetEntries():
    return 2


class EntryNotebook(wx.Notebook):
    
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        self.AddPage(PersonUI.PersonPanel(self), "Person")
        self.AddPage(SourceUI.SourcePanel(self), "Source")
        self.AddPage(MatrixUI.MatrixPanel(self), "Matrix")

########################################################################


class NestedEntryPanel(wx.Panel):
    """
    Panel contains multiple 'Entry' tabs
    """
    def __init__(self, parent, EntryInfo):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        NumEntries = self.NumEntries = EntryInfo # GetEntries()
        
        nestedNotebook = self.nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        
        self.addEntryButton = wx.Button(self, -1, "Add Entry")
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonAddEntry, self.addEntryButton)
        
        topSizer = self.topSizer = wx.BoxSizer(wx.HORIZONTAL)
        topSizer.Add(self.addEntryButton, 0, wx.ALIGN_RIGHT)

        for i in range(1, NumEntries+1):
            nestedNotebook.AddPage(EntryNotebook(nestedNotebook), "Entry " + str(i))
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSizer, 0, wx.ALIGN_RIGHT)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
    # When the user selects something, we go here.
    def OnButtonAddEntry(self, evt):
        self.NumEntries += 1
        self.nestedNotebook.AddPage(EntryNotebook(self.nestedNotebook), "Entry " + str(self.NumEntries))
        
        
        