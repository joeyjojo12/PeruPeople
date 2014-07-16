import wx
import PeruConstants
from database import SourceDB, SourceEntryDB


def getSourceInfo(sourcePage):
    return [str(sourcePage.SourceID),
            str(sourcePage.DocumentType.GetValue()),
            sourcePage.BookTitle.GetValue(),
            sourcePage.BookAuthor1.GetValue(),
            sourcePage.BookAuthor2.GetValue(),
            sourcePage.BookAuthor3.GetValue(),
            sourcePage.BookAuthor4.GetValue(),
            sourcePage.BookAuthor5.GetValue(),
            sourcePage.BookPublisher.GetValue(),            sourcePage.BookPubPlace.GetValue(),
            str(sourcePage.BookYear.GetValue()),
            sourcePage.ArticleTitle.GetValue(),
            sourcePage.ArticleAuthor1.GetValue(),
            sourcePage.ArticleAuthor2.GetValue(),
            sourcePage.ArticleAuthor3.GetValue(),
            sourcePage.ArticleAuthor4.GetValue(),
            sourcePage.ArticleAuthor5.GetValue(),
            sourcePage.ArticlePublication.GetValue(),
            str(sourcePage.ArticleYear.GetValue()),
            sourcePage.ArticleVolume.GetValue(),
            sourcePage.ArticleIssue.GetValue(),
            sourcePage.ArchiveName.GetValue(),
            sourcePage.ArchiveCollection.GetValue(),
            str(sourcePage.ArchiveYear.GetValue()),
            str(sourcePage.ArchiveMonth.GetValue()),
            str(sourcePage.ArchiveDay.GetValue()),
            sourcePage.ArchiveStack.GetValue(),
            sourcePage.ArchiveExpedientes.GetValue()]
    
def saveSource(database, sourcePage):
        return SourceDB.InsertUpdateSource(database, getSourceInfo(sourcePage))
    
def getSourceEntryInfo(sourcePage):
    return [str(sourcePage.SourceEntryID),
            str(sourcePage.DocumentType.GetValue()),
            sourcePage.BookPageNumbers.GetValue(),
            sourcePage.BookNotes.GetValue(),
            sourcePage.ArticlePageNumbers.GetValue(),
            sourcePage.ArticleNotes.GetValue(),
            sourcePage.ArchivePageNumbers.GetValue(),
            sourcePage.ArchivePhotoReference.GetValue(),
            sourcePage.ArchiveNotes.GetValue()]
    
def saveSourceEntry(database, sourcePage):
        return SourceEntryDB.InsertUpdateSourceEntry(database, getSourceEntryInfo(sourcePage))

class SourcePanel(wx.Panel):
    def __init__(self, parent, SourceID, SourceEntryID):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        if(SourceID > 0):
            self.SourceID = SourceID
            self.SourceFields = SourceDB.ReadSource(SourceID)[1][0]
        else:
            SourceID = self.SourceID = ''
            self.SourceFields = []
        
        if(SourceEntryID > 0):
            self.SourceEntryID = SourceEntryID
            self.SourceEntryFields = SourceEntryDB.ReadSourceEntry(SourceEntryID)[1][0]
        else:
            SourceEntryID = self.SourceEntryID = ''
            self.SourceEntryFields = []        

        DocumentType = self.DocumentType = wx.ComboBox(self, 500, PeruConstants.DEFAULT_DOCUMENT, (90, 50), (120, -1), PeruConstants.DOCUMENT_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        self.Bind(wx.EVT_COMBOBOX, self.OnChangeType, self.DocumentType)
        
        # Book fields
        bookList = self.bookList = []
        BookTitle = self.BookTitle = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Title :"), BookTitle ))
        BookAuthor1 = self.BookAuthor1 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 1 :"), BookAuthor1))
        BookAuthor2 = self.BookAuthor2 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 2 :"), BookAuthor2))
        BookAuthor3 = self.BookAuthor3 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 3 :"), BookAuthor3))
        BookAuthor4 = self.BookAuthor4 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 4 :"), BookAuthor4))
        BookAuthor5 = self.BookAuthor5 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 5 :"), BookAuthor5))
        BookPublisher = self.BookPublisher = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Publisher :"), BookPublisher))
        BookPubPlace = self.BookPubPlace = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Publisher Location :"), BookPubPlace))
        BookYear = self.BookYear = wx.TextCtrl(self, size=(100,-1))
        bookList.append((wx.StaticText(self, label="Year :"), BookYear))
        BookPageNumbers = self.BookPageNumbers = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Page Numbers :"), BookPageNumbers))        
        BookNotes = self.BookNotes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        bookList.append((wx.StaticText(self, label="Notes :"), BookNotes))
        
        # Article fields
        articleList = self.articleList = []
        ArticleTitle = self.ArticleTitle = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Title :"), ArticleTitle ))
        ArticleAuthor1 = self.ArticleAuthor1 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 1 :"), ArticleAuthor1))
        ArticleAuthor2 = self.ArticleAuthor2 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 2 :"), ArticleAuthor2))
        ArticleAuthor3 = self.ArticleAuthor3 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 3 :"), ArticleAuthor3))
        ArticleAuthor4 = self.ArticleAuthor4 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 4 :"), ArticleAuthor4))
        ArticleAuthor5 = self.ArticleAuthor5 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 5 :"), ArticleAuthor5))
        ArticlePublication = self.ArticlePublication = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Publication :"), ArticlePublication))
        ArticleYear = self.ArticleYear = wx.TextCtrl(self, size=(100,-1))
        articleList.append((wx.StaticText(self, label="Year :"), ArticleYear))
        ArticleVolume = self.ArticleVolume = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Volume :"), ArticleVolume))
        ArticleIssue = self.ArticleIssue = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Issue :"), ArticleIssue))
        ArticlePageNumbers = self.ArticlePageNumbers = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Page Numbers :"), ArticlePageNumbers))
        ArticleNotes = self.ArticleNotes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        articleList.append((wx.StaticText(self, label="Notes :"), ArticleNotes))
        
        # Archive fields
        archiveList = self.archiveList = []
        ArchiveName = self.ArchiveName = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Archive Name :"), ArchiveName))
        ArchiveCollection = self.ArchiveCollection = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Collection :"), ArchiveCollection ))
        ArchiveYear = self.ArchiveYear = wx.TextCtrl(self, size=(100,-1))
        archiveList.append((wx.StaticText(self, label="Year :"), ArchiveYear))
        ArchiveMonth = self.ArchiveMonth = wx.TextCtrl(self, size=(100,-1))
        archiveList.append((wx.StaticText(self, label="Month :"), ArchiveMonth))
        ArchiveDay = self.ArchiveDay = wx.TextCtrl(self, size=(100,-1))
        archiveList.append((wx.StaticText(self, label="Day :"), ArchiveDay))        
        ArchiveStack = self.ArchiveStack = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Stack :"), ArchiveStack ))
        ArchiveExpedientes = self.ArchiveExpedientes = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Expedientes :"), ArchiveExpedientes ))
        ArchivePageNumbers = self.ArchivePageNumbers = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Page Numbers :"), ArchivePageNumbers))
        ArchivePhotoReference = self.ArchivePhotoReference = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        archiveList.append((wx.StaticText(self, label="Photo Reference(s) :"), ArchivePhotoReference))
        ArchiveNotes = self.ArchiveNotes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        archiveList.append((wx.StaticText(self, label="Notes :"), ArchiveNotes))
        
        SourceLists = self.SourceLists = [bookList, articleList, archiveList]
       
        space = 6
        infoSizer = self.infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        self.SelectSourceButton = wx.Button(self, -1, "Select Source")
        self.Bind(wx.EVT_BUTTON, self.OnButtonSelectSource, self.SelectSourceButton)
        
        self.ClearFieldsButton = wx.Button(self, -1, "New Source")
        self.Bind(wx.EVT_BUTTON, self.OnButtonClearFields, self.ClearFieldsButton)
       
        #Initially set document type as archive
        self.ArrangeFields(PeruConstants.ARCHIVE)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        
        #Populate fields with content from current person
        if(SourceID != ''):
            self.PopulateFields()
            self.ArrangeFields(PeruConstants.DOCUMENT_LIST.index(DocumentType.GetValue()))

        self.SetSizer(sizer)
        
    # Arrange fields, removing fields that are not required for the specified document type.
    def ArrangeFields(self, docType):
        self.infoSizer.Clear()        
        
        self.DocumentType.Show()
        self.infoSizer.Add(self.DocumentType,(0,0))        
        
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.buttonSizer.Add(self.SelectSourceButton, 0, wx.ALIGN_LEFT)
        self.buttonSizer.Add(self.ClearFieldsButton, 0, wx.ALIGN_RIGHT)
        self.infoSizer.Add(self.buttonSizer,(0,1))
        
        for i in range(len(self.SourceLists)):
            k = 1 #Giving a gap
            if i == docType:
                for j in range(len(self.SourceLists[i])):
                    if (j == len(self.SourceLists[i]) - 2) and (docType == PeruConstants.ARCHIVE):
                        #This takes care of the photo reference field    
                        self.infoSizer.Add(self.SourceLists[i][len(self.SourceLists[i])-2][0],     (k+1,0))
                        self.infoSizer.Add(self.SourceLists[i][len(self.SourceLists[i])-2][1],     (k+1,1), (4,2), wx.EXPAND)
                        k += 4
                        
                    elif (j == len(self.SourceLists[i]) - 1):
                        #This takes care of the notes field    
                        self.infoSizer.Add(self.SourceLists[i][len(self.SourceLists[i])-1][0],     (k+1,0))
                        self.infoSizer.Add(self.SourceLists[i][len(self.SourceLists[i])-1][1],     (k+1,1), (4,2), wx.EXPAND)
                        k += 4
                                                
                    else:
                        self.infoSizer.Add(self.SourceLists[i][j][0],    (k+1,0))
                        self.infoSizer.Add(self.SourceLists[i][j][1],    (k+1,1))
                    
                    self.SourceLists[i][j][0].Show()
                    self.SourceLists[i][j][1].Show()
                    
                    k += 1
            else:
                for j in range(len(self.SourceLists[i])):
                    self.SourceLists[i][j][0].Hide()
                    self.SourceLists[i][j][1].Hide()
                
        self.infoSizer.Layout()
        
            
    def PopulateFields(self):
        self.DocumentType.SetStringSelection(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('DocumentType')])
        self.BookTitle.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookTitle')])
        self.BookAuthor1.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor1')])
        self.BookAuthor2.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor2')])
        self.BookAuthor3.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor3')])
        self.BookAuthor4.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor4')])
        self.BookAuthor5.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor5')])
        self.BookPublisher.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookPublisher')])
        self.BookPubPlace.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookPubPlace')])
        self.BookYear.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookYear')]))
        self.BookPageNumbers.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('BookPageNumbers')])
        self.BookNotes.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('BookNotes')])
        
        self.ArticleTitle.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleTitle')])
        self.ArticleAuthor1.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor1')])
        self.ArticleAuthor2.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor2')])
        self.ArticleAuthor3.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor3')])
        self.ArticleAuthor4.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor4')])
        self.ArticleAuthor5.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor5')])
        self.ArticlePublication.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticlePublication')])
        self.ArticleYear.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleYear')]))
        self.ArticleVolume.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleVolume')])
        self.ArticleIssue.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleIssue')])
        self.ArticlePageNumbers.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArticlePageNumbers')])
        self.ArticleNotes.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArticleNotes')])
        
        self.ArchiveName.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveName')])
        self.ArchiveCollection.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveCollection')])
        self.ArchiveYear.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveYear')]))
        self.ArchiveMonth.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveMonth')]))
        self.ArchiveDay.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveDay')]))
        self.ArchiveStack.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveStack')])
        self.ArchiveExpedientes.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveExpedientes')])
        self.ArchivePageNumbers.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchivePageNumbers')])
        self.ArchivePhotoReference.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchivePhotoReference')])
        self.ArchiveNotes.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchiveNotes')])
                
    def ClearFields(self):
        for tupple in self.bookList:
            tupple[1].Clear()   
        for tupple in self.articleList:
            tupple[1].Clear()   
        for tupple in self.archiveList:
            tupple[1].Clear()        
        
    def OnChangeType(self, evt):
        self.ArrangeFields(self.DocumentType.GetSelection())
        
    def OnButtonSelectSource(self, evt):
        print("select")
        
    def OnButtonClearFields(self, evt):
        documentType = PeruConstants.DOCUMENT_LIST.index(self.DocumentType.GetValue())
        
        self.SourceID = ''
        self.SourceFields = []
        self.SourceEntryID = ''
        self.SourceEntryFields = []
        self.ClearFields()
        self.ArrangeFields(documentType)
        
        