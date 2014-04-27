import wx
import PersonUI, SourceUI, MatrixUI
import PeruConstants
from database import EntryDB
from database import PeruDB

def GetEntries():
    return 2


class EntryNotebook(wx.Notebook):
    
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        self.AddPage(PersonUI.PersonPanel(self), "Person")
        self.AddPage(SourceUI.SourcePanel(self), "Source")
        self.AddPage(MatrixUI.MatrixPanel(self), "Matrix")


class NestedEntryPanel(wx.Panel):
    """
    Panel contains multiple 'Entry' tabs
    """
    def __init__(self, parent, NewGroup, PersonGroupID):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        if(NewGroup):
            #do this
            NumEntries = self.NumEntries = 1 # GetEntries()
        else:
            NumEntries = self.NumEntries = 1 # GetEntries()
            
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

        noErrors = True
        
        database = PeruDB.PeruDB()

        for i in range(self.nestedNotebook.GetPageCount()):
            #Save Person for this entry
            result = PersonUI.savePerson(database, self.nestedNotebook.GetPage(i).GetPage(0))
            if result[0] != 0:
                print(result[1])
                noErrors = False
                break
            Person = result[1]

            #Save Source for this entry
            result = SourceUI.saveSource(database, self.nestedNotebook.GetPage(i).GetPage(1))
            if result[0] != 0:
                print(result[1])
                noErrors = False
                break
            Source = result[1]

            #Save Matrix for this entry
            result = MatrixUI.saveMatrix(database, self.nestedNotebook.GetPage(i).GetPage(2))
            if result[0] != 0:
                print(result[1])
                noErrors = False
                break
            Matrix = result[1]
            
            EntryDB.InsertUpdateEntry(database, ['', self.PersonGroupID, Person, Source, Matrix])
            
        if(noErrors):
            database.commit()
        else:
            database.rollback()

        database.closeDB()
            
        
        
        
