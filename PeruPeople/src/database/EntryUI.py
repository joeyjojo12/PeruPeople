import wx
import PeruConstants, PersonUI, SourceUI, MatrixUI, EntryDB

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
    def __init__(self, parent, EntryInfo, PersonGroupID):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        NumEntries = self.NumEntries = EntryInfo # GetEntries()        
        self.PersonGroupID = PersonGroupID
        
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
    
    def SaveEntries(self):

        for i in range(self.nestedNotebook.GetPageCount()):
            result = PersonUI.savePerson(self.nestedNotebook.GetPage(i).GetPage(0))
            if result[0] != 0:
                print(result[1])
                break
            Person = result[1]
            
            EntryDB.InsertUpdateEntry(['', self.PersonGroupID, Person, 0, 0])
            
            
            #SourceID = SourceUI.saveMatrix(self.nestedNotebook.GetPage(i).GetPage(1))
            #MatrixID = MatrixUI.saveMatrix(self.nestedNotebook.GetPage(i).GetPage(2))
        
        
        