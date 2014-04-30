import wx
import PeruConstants
from database import SourceDB


def getSourceInfo(sourcePage):
    return [str(sourcePage.SourceID),
            str(sourcePage.Type.GetValue()),
            str(sourcePage.Citation.GetValue()),
            str(sourcePage.Archive.GetValue()),
            str(sourcePage.Stack.GetValue()),
            str(sourcePage.PageNumbers.GetValue()),
            str(sourcePage.Author.GetValue()),
            str(sourcePage.DocNameTitle.GetValue()),
            str(sourcePage.Publisher.GetValue()),
            str(sourcePage.PubPlace.GetValue()),
            str(sourcePage.Year.GetValue()),
            str(sourcePage.ReferencedByFirst.GetValue()),
            str(sourcePage.ReferencedByLast.GetValue()),
            str(sourcePage.Notes.GetValue())]
    
def saveSource(database, sourcePage):
        return SourceDB.InsertUpdateSource(database, getSourceInfo(sourcePage))

class SourcePanel(wx.Panel):
    def __init__(self, parent, SourceID):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        if(SourceID > 0):
            self.SourceID = SourceID
            self.SourceFields = SourceDB.ReadSource(SourceID)[1][0]
        else:
            SourceID = self.SourceID = ''
            self.SourceFields = self.SourceFields = []
        
        fieldList = []

        Type = self.Type = wx.ComboBox(self, 500, PeruConstants.DEFAULT_DOCUMENT, (90, 50), (150, -1), PeruConstants.DOCUMENT_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        fieldList.append((wx.StaticText(self, label="Type :"), Type))

        Citation = self.Citation = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Citation :"), Citation))

        Archive = self.Archive = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Archive :"), Archive))
        
        Stack = self.Stack = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Stack :"), Stack ))

        PageNumbers = self.PageNumbers = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Page Numbers :"), PageNumbers))

        Author = self.Author = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Author :"), Author))

        DocNameTitle = self.DocNameTitle = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Document Name :"), DocNameTitle))

        Publisher = self.Publisher = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Place of Publication :"), Publisher))

        PubPlace = self.PubPlace = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Place of Publication :"), PubPlace))

        Year = self.Year = wx.TextCtrl(self, size=(100,-1))
        fieldList.append((wx.StaticText(self, label="Year :"), Year))

        ReferencedByFirst = self.ReferencedByFirst = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Referenced By First Name :"), ReferencedByFirst))

        ReferencedByLast = self.ReferencedByLast = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Referenced By Last Name :"), ReferencedByLast))
        
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        fieldList.append((wx.StaticText(self, label="Notes :"), Notes))
       
        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        for i in range(len(fieldList) - 1):
            infoSizer.Add(fieldList[i][0],    (i+1,0))
            infoSizer.Add(fieldList[i][1],    (i+1,1))
        
        #Add notes    
        infoSizer.Add(fieldList[len(fieldList)-1][0],     (len(fieldList),0))
        infoSizer.Add(fieldList[len(fieldList)-1][1],     (len(fieldList),1), (4,2), wx.EXPAND)
       
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        
        #Populate fields with content from current person
        if(SourceID != ''):
            self.PopulateFields()

        self.SetSizer(sizer)
            
    def PopulateFields(self):
        self.Type.SetStringSelection(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Type')])
        self.Citation.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Citation')])
        self.Archive.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Archive')])
        self.Stack.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Stack')])
        self.PageNumbers.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('PageNumbers')])
        self.Author.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Author')])
        self.DocNameTitle.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('DocNameTitle')])
        self.Publisher.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Publisher')])
        self.PubPlace.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('PubPlace')])
        self.Year.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Year')]))
        self.ReferencedByFirst.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ReferencedByFirst')])
        self.ReferencedByLast.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ReferencedByLast')])
        self.Notes.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Notes')])
        