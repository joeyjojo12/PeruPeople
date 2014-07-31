import wx
import sys
import PersonUI, SourceUI, MatrixUI
import PeruConstants
from database import EntryDB
from database import PeruDB

class EntryNotebook(wx.Notebook):
    
    def __init__(self, parent, currentEntry):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        
        if(len(currentEntry) > 0):
            self.EntryID = currentEntry[PeruConstants.ENTRY_FIELDS.index('EntryID')]
            self.AddPage(PersonUI.PersonPanel(self, currentEntry[PeruConstants.ENTRY_FIELDS.index('PersonID')]), "Person")
            self.AddPage(SourceUI.SourcePanel(self, currentEntry[PeruConstants.ENTRY_FIELDS.index('SourceID')], currentEntry[PeruConstants.ENTRY_FIELDS.index('SourceEntryId')]), "Source")
            self.AddPage(MatrixUI.MatrixPanel(self, currentEntry[PeruConstants.ENTRY_FIELDS.index('MatrixID')]), "Matrix")            
        else:
            self.EntryID = ''
            self.AddPage(PersonUI.PersonPanel(self, 0), "Person")
            self.AddPage(SourceUI.SourcePanel(self, 0, 0), "Source")
            self.AddPage(MatrixUI.MatrixPanel(self, 0), "Matrix")


class NestedEntryPanel(wx.Panel):
    """
    Panel contains multiple 'Entry' tabs
    """
    def __init__(self, parent, NewGroup, PersonGroupID):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
            
        self.PersonGroupID = PersonGroupID
        self.NewGroup = NewGroup
        self.NumEntries = 1
        EntryList = self.EntryList = []
        
        if(NewGroup != True):
            EntryList = EntryDB.ReadEntries(PersonGroupID)[1]
            self.NumEntries = len(EntryList)
        
        nestedNotebook = self.nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        
        self.addEntryButton = wx.Button(self, -1, "Add Entry")
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonAddEntry, self.addEntryButton)
        
        topSizer = self.topSizer = wx.BoxSizer(wx.HORIZONTAL)
        topSizer.Add(self.addEntryButton, 0, wx.ALIGN_RIGHT)
        
        if(len(EntryList) > 0):
            for i in range(len(EntryList)):
                nestedNotebook.AddPage(EntryNotebook(nestedNotebook, EntryList[i]), "Entry " + str(i+1))
        else:
            self.NumEntries = 1
            nestedNotebook.AddPage(EntryNotebook(nestedNotebook, []), "Entry 1")

        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.deleteButton = wx.Button(self, -1, "Delete Entry")
        self.buttonSizer.Add(self.deleteButton, 0, wx.ALIGN_RIGHT)
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonDelete, self.deleteButton)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSizer, 0, wx.ALIGN_RIGHT)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(self.buttonSizer, 2, wx.ALIGN_RIGHT)

        self.SetSizer(sizer)
        
    # When the user selects something, we go here.
    def OnButtonAddEntry(self, evt):
        self.NumEntries += 1
        self.nestedNotebook.AddPage(EntryNotebook(self.nestedNotebook, []), "Entry " + str(self.NumEntries))
        
    # When the user selects something, we go here.
    def OnButtonDelete(self, evt):
        noErrors = True        
        database = PeruDB.PeruDB()
                
        try:
            EntryDB.DeleteEntry(database, self.nestedNotebook.GetCurrentPage().EntryID)                
        except:
            print("Database Error!")
            print(sys.exc_info()[0])
            noErrors = False
            
        if(noErrors):
            database.commit()
            self.nestedNotebook.DeletePage(self.nestedNotebook.GetSelection())
        else:
            database.rollback()
        
    
    def SaveEntries(self):

        noErrors = True
        
        database = PeruDB.PeruDB()
        ErrorMessage = ""

        try:
            for i in range(self.nestedNotebook.GetPageCount()):
                #Save Person for this entry
                result = PersonUI.savePerson(database, self.nestedNotebook.GetPage(i).GetPage(0))
                if result[0] != 0:
                    print(result[1])
                    ErrorMessage = result[1]
                    noErrors = False
                    break
                Person = result[1]
    
                #Save Source for this entry
                result = SourceUI.saveSource(database, self.nestedNotebook.GetPage(i).GetPage(1))
                if result[0] != 0:
                    print(result[1])
                    ErrorMessage = result[1]
                    noErrors = False
                    break
                Source = result[1]
    
                #Save SourceEntry for this entry
                result = SourceUI.saveSourceEntry(database, self.nestedNotebook.GetPage(i).GetPage(1))
                if result[0] != 0:
                    print(result[1])
                    ErrorMessage = result[1]
                    noErrors = False
                    break
                SourceEntry = result[1]
    
                #Save Matrix for this entry
                result = MatrixUI.saveMatrix(database, self.nestedNotebook.GetPage(i).GetPage(2))
                if result[0] != 0:
                    print(result[1])
                    ErrorMessage = result[1]
                    noErrors = False
                    break
                Matrix = result[1]
                
                result = EntryDB.InsertUpdateEntry(database, [self.nestedNotebook.GetPage(i).EntryID, self.PersonGroupID, Person, Source, SourceEntry, Matrix])
                if result[0] != 0:
                    print(result[1])
                    ErrorMessage = result[1]
                    noErrors = False
                    break
                
        except:
            print("Database Error!")
            noErrors = False
            
        if(noErrors):
            database.commit()
            self.DisplayMessage(PeruConstants.SUCCESSFULL_SAVING_HEADER, PeruConstants.SUCCESSFULL_SAVING_MESSAGE)
        else:
            database.rollback()
            self.DisplayMessage(PeruConstants.ERROR_SAVING_HEADER, PeruConstants.ERROR_SAVING_MESSAGE + ErrorMessage)

        database.closeDB()
        
    def DisplayMessage(self, Header, Message):
        
        dlg = wx.MessageDialog(self, Message, Header,
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
            
        
        
        
