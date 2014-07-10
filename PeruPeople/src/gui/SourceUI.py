import wx
import PeruConstants
from database import SourceDB

ARCHIVAL = 1
BOOK = 2
ARTICLE = 4


def getSourceInfo(sourcePage):
    return [str(sourcePage.SourceID),
            str(sourcePage.Type.GetValue()),
            sourcePage.Citation.GetValue(),
            sourcePage.Archive.GetValue(),
            sourcePage.Collection.GetValue(),
            sourcePage.Stack.GetValue(),
            sourcePage.Expedientes.GetValue(),
            sourcePage.PageNumbers.GetValue(),
            sourcePage.Author.GetValue(),
            sourcePage.DocNameTitle.GetValue(),
            sourcePage.Publisher.GetValue(),
            sourcePage.PubPlace.GetValue(),
            str(sourcePage.Year.GetValue()),
            sourcePage.ReferencedByFirst.GetValue(),
            sourcePage.ReferencedByLast.GetValue(),
            sourcePage.Notes.GetValue()]
    
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
        
        fieldList = self.fieldList = []

        Type = self.Type = wx.ComboBox(self, 500, PeruConstants.DEFAULT_DOCUMENT, (90, 50), (150, -1), PeruConstants.DOCUMENT_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        self.Bind(wx.EVT_COMBOBOX, self.OnChangeType, self.Type)
        fieldList.append((wx.StaticText(self, label="Type :"), Type))
        
        Citation = self.Citation = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Citation :"), Citation ))

        Archive = self.Archive = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Archive :"), Archive, ARCHIVAL))

        Collection = self.Collection = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Collection :"), Collection, ARCHIVAL))
        
        Stack = self.Stack = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Stack :"), Stack, ARCHIVAL ))
        
        Expedientes = self.Expedientes = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Expedientes :"), Expedientes, ARCHIVAL ))

        PageNumbers = self.PageNumbers = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Page Numbers :"), PageNumbers, ARCHIVAL ))

        Author = self.Author = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Author :"), Author, BOOK))

        DocNameTitle = self.DocNameTitle = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Document Name :"), DocNameTitle, BOOK))

        Publisher = self.Publisher = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Publisher :"), Publisher))

        PubPlace = self.PubPlace = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Place of Publication :"), PubPlace))

        Year = self.Year = wx.TextCtrl(self, size=(100,-1))
        fieldList.append((wx.StaticText(self, label="Year :"), Year, ARCHIVAL, BOOK))

        ReferencedByFirst = self.ReferencedByFirst = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Referenced By First Name :"), ReferencedByFirst))

        ReferencedByLast = self.ReferencedByLast = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Referenced By Last Name :"), ReferencedByLast))
        
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        fieldList.append((wx.StaticText(self, label="Notes :"), Notes))
       
        space = 6
        infoSizer = self.infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
       
        #Initially set document type as book
        self.ArrangeFields(BOOK)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        
        #Populate fields with content from current person
        if(SourceID != ''):
            self.PopulateFields()

        self.SetSizer(sizer)
        
    # Arrange fields, removing fields that are not required for the specified document type.
    def ArrangeFields(self, docType):
        self.infoSizer.Clear()
        j=0
        for i in range(len(self.fieldList) - 1):
            if(len(self.fieldList[i]) > 2 and (self.fieldList[i][2] & docType) > 0):
                self.fieldList[i][0].Hide()
                self.fieldList[i][1].Hide()
                j-=1                
            else:
                self.fieldList[i][0].Show()
                self.fieldList[i][1].Show()
                self.infoSizer.Add(self.fieldList[i][0],    (j+1,0))
                self.infoSizer.Add(self.fieldList[i][1],    (j+1,1))
            j+=1
        
        #Add notes    
        self.infoSizer.Add(self.fieldList[len(self.fieldList)-1][0],     (j+1,0))
        self.infoSizer.Add(self.fieldList[len(self.fieldList)-1][1],     (j+1,1), (4,2), wx.EXPAND)
        
        self.infoSizer.Layout()
        
            
    def PopulateFields(self):
        self.Type.SetStringSelection(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Type')])
        self.Citation.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Citation')])
        self.Archive.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Archive')])
        self.Collection.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Collection')])
        self.Stack.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Stack')])
        self.Expedientes.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Expedientes')])
        self.PageNumbers.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('PageNumbers')])
        self.Author.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Author')])
        self.DocNameTitle.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('DocNameTitle')])
        self.Publisher.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Publisher')])
        self.PubPlace.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('PubPlace')])
        self.Year.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Year')]))
        self.ReferencedByFirst.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ReferencedByFirst')])
        self.ReferencedByLast.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ReferencedByLast')])
        self.Notes.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('Notes')])
        
    def OnChangeType(self, evt):
        self.ArrangeFields(self.Type.GetSelection())
        
        