import wx
import PeruConstants


class EntryPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)


class NestedEntryPanel(wx.Panel):
    """
    Panel contains multiple 'Entry' tabs
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.NumEntries = 1
        
        nestedNotebook = self.nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        
        self.addEntryButton = wx.Button(self, -1, "Add Entry")
        self.buttonSizer.Add(self.addEntryButton, 0, wx.ALIGN_RIGHT)
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonAddEntry, self.saveCaseButton)
        
        topSizer = self.topSizer = wx.BoxSizer(wx.HORIZONTAL)

        #for i in range(1,self.numDefendants.GetValue()+1):
        #@nestedNotebook.AddPage(DefendantPanel(nestedNotebook), "Defendant 1")
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSizer, 0, wx.ALIGN_LEFT)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
    # When the user selects something, we go here.
    def OnButtonAddEntry(self, evt):
        self.NumEntries += 1        
        self.nestedNotebook.AddPage(EntryPanel(self.nestedNotebook), "Entry " + self.NumEntries)