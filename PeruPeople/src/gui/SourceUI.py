import wx
import PeruConstants, SourceListUI
from database import SourceDB, SourceEntryDB


def getSourceInfo(sourcePage):
    returnList = []
    documentType = sourcePage.DocumentType.GetValue()
    
    returnList.append(str(sourcePage.SourceID))
    returnList.append(str(sourcePage.DocumentType.GetValue()))
    
    for i in range(len(PeruConstants.BOOK_FIELDS)):
        if documentType == 'Book':
            returnList.append(sourcePage.bookList[i][1].GetValue())
        else:
            returnList.append("")
    
    for i in range(len(PeruConstants.ARTICLE_FIELDS)):
        if documentType == 'Article':
            returnList.append(sourcePage.articleList[i][1].GetValue())
        else:
            returnList.append("")
    
    for i in range(len(PeruConstants.ARCHIVE_FIELDS)):
        if documentType == 'Archive':
            returnList.append(sourcePage.archiveList[i][1].GetValue())
        else:
            returnList.append("")
            
    return returnList
    
def saveSource(database, sourcePage):
    # If the source hasn't changed, don't update. Just return the ID.
    if(sourcePage.SourceChanged):
        return SourceDB.InsertUpdateSource(database, getSourceInfo(sourcePage))
    else:
        return [0,sourcePage.SourceID]
    
def getSourceEntryInfo(sourcePage):
    returnList = []
    documentType = sourcePage.DocumentType.GetValue()
    
    returnList.append(str(sourcePage.SourceEntryID))
    returnList.append(str(sourcePage.DocumentType.GetValue()))
    
    for i in range(len(PeruConstants.BOOK_FIELDS), len(PeruConstants.BOOK_FIELDS) + len(PeruConstants.BOOK_ENTRY_FIELDS)):
        if documentType == 'Book':
            returnList.append(sourcePage.bookList[i][1].GetValue())
        else:
            returnList.append("")
    
    for i in range(len(PeruConstants.ARTICLE_FIELDS), len(PeruConstants.ARTICLE_FIELDS) + len(PeruConstants.ARTICLE_ENTRY_FIELDS)):
        if documentType == 'Article':
            returnList.append(sourcePage.articleList[i][1].GetValue())
        else:
            returnList.append("")
    
    for i in range(len(PeruConstants.ARCHIVE_FIELDS), len(PeruConstants.ARCHIVE_FIELDS) + len(PeruConstants.ARCHIVE_ENTRY_FIELDS)):
        if documentType == 'Archive':
            returnList.append(sourcePage.archiveList[i][1].GetValue())
        else:
            returnList.append("")
    
    return returnList
    
def saveSourceEntry(database, sourcePage):
    return SourceEntryDB.InsertUpdateSourceEntry(database, getSourceEntryInfo(sourcePage))

class SourcePanel(wx.Panel):
    def __init__(self, parent, SourceID, SourceEntryID):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        if(SourceID > 0):
            self.SourceID = self.initialSourceID = SourceID
            self.SourceFields = SourceDB.ReadSource(SourceID)[1][0]
            self.initialType = self.SourceFields[PeruConstants.SOURCE_FIELDS.index('DocumentType')]
        else:
            SourceID = self.SourceID = self.initialSourceID = ''
            self.SourceFields = []
            self.initialType = ''
            self.SourceChanged = True
        
        if(SourceEntryID > 0):
            self.SourceEntryID = SourceEntryID
            self.SourceEntryFields = SourceEntryDB.ReadSourceEntry(SourceEntryID)[1][0]
        else:
            SourceEntryID = self.SourceEntryID = ''
            self.SourceEntryFields = []        

        DocumentType = self.DocumentType = wx.ComboBox(self, 500, PeruConstants.DEFAULT_DOCUMENT, (90, 50), (120, -1), PeruConstants.DOCUMENT_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        self.Bind(wx.EVT_COMBOBOX, self.OnChangeType, self.DocumentType)
        self.DocumentType.SetStringSelection(PeruConstants.DEFAULT_DOCUMENT)
        
        # Book fields
        bookList = self.bookList = []
        
        BookTitle = self.BookTitle = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Title :"), BookTitle ))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookTitle)
        
        BookAuthor1 = self.BookAuthor1 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 1 :"), BookAuthor1))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookAuthor1)
        
        BookAuthor2 = self.BookAuthor2 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 2 :"), BookAuthor2))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookAuthor2)
        
        BookAuthor3 = self.BookAuthor3 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 3 :"), BookAuthor3))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookAuthor3)
        
        BookAuthor4 = self.BookAuthor4 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 4 :"), BookAuthor4))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookAuthor4)
        
        BookAuthor5 = self.BookAuthor5 = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Author 5 :"), BookAuthor5))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookAuthor5)
        
        BookPublisher = self.BookPublisher = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Publisher :"), BookPublisher))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookPublisher)
        
        BookPubPlace = self.BookPubPlace = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Publisher Location :"), BookPubPlace))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookPubPlace)
        
        BookYear = self.BookYear = wx.TextCtrl(self, size=(100,-1))
        bookList.append((wx.StaticText(self, label="Year :"), BookYear))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, BookYear)
        
        BookPageNumbers = self.BookPageNumbers = wx.TextCtrl(self, size=(400,-1))
        bookList.append((wx.StaticText(self, label="Page Numbers :"), BookPageNumbers))        
        
        BookNotes = self.BookNotes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        bookList.append((wx.StaticText(self, label="Notes :"), BookNotes))
        
        # Article fields
        articleList = self.articleList = []
        
        ArticleTitle = self.ArticleTitle = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Title :"), ArticleTitle ))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleTitle)
        
        ArticleAuthor1 = self.ArticleAuthor1 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 1 :"), ArticleAuthor1))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleAuthor1)
        
        ArticleAuthor2 = self.ArticleAuthor2 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 2 :"), ArticleAuthor2))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleAuthor2)
        
        ArticleAuthor3 = self.ArticleAuthor3 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 3 :"), ArticleAuthor3))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleAuthor3)
        
        ArticleAuthor4 = self.ArticleAuthor4 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 4 :"), ArticleAuthor4))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleAuthor4)
        
        ArticleAuthor5 = self.ArticleAuthor5 = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Author 5 :"), ArticleAuthor5))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleAuthor5)
        
        ArticlePublication = self.ArticlePublication = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Publication :"), ArticlePublication))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticlePublication)
        
        ArticleYear = self.ArticleYear = wx.TextCtrl(self, size=(100,-1))
        articleList.append((wx.StaticText(self, label="Year :"), ArticleYear))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleYear)
        
        ArticleVolume = self.ArticleVolume = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Volume :"), ArticleVolume))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleVolume)
        
        ArticleIssue = self.ArticleIssue = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Issue :"), ArticleIssue))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArticleIssue)
        
        ArticlePageNumbers = self.ArticlePageNumbers = wx.TextCtrl(self, size=(400,-1))
        articleList.append((wx.StaticText(self, label="Page Numbers :"), ArticlePageNumbers))
        
        ArticleNotes = self.ArticleNotes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        articleList.append((wx.StaticText(self, label="Notes :"), ArticleNotes))
        
        # Archive fields
        archiveList = self.archiveList = []
        
        ArchiveName = self.ArchiveName = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Archive Name :"), ArchiveName))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArchiveName)
        
        ArchiveCollection = self.ArchiveCollection = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Collection :"), ArchiveCollection ))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArchiveCollection)
        
        ArchiveYear = self.ArchiveYear = wx.TextCtrl(self, size=(100,-1))
        archiveList.append((wx.StaticText(self, label="Year :"), ArchiveYear))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArchiveYear)
        
        ArchiveMonth = self.ArchiveMonth = wx.TextCtrl(self, size=(100,-1))
        archiveList.append((wx.StaticText(self, label="Month :"), ArchiveMonth))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArchiveMonth)
        
        ArchiveDay = self.ArchiveDay = wx.TextCtrl(self, size=(100,-1))
        archiveList.append((wx.StaticText(self, label="Day :"), ArchiveDay))  
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArchiveDay)
              
        ArchiveStack = self.ArchiveStack = wx.TextCtrl(self, size=(400,-1))
        archiveList.append((wx.StaticText(self, label="Stack :"), ArchiveStack ))
        self.Bind(wx.EVT_TEXT, self.SourceHasChanged, ArchiveStack)
        
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
            self.SourceChanged = False

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
        
    def PopulateSourceFields(self):
        self.BookTitle.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookTitle')])
        self.BookAuthor1.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor1')])
        self.BookAuthor2.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor2')])
        self.BookAuthor3.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor3')])
        self.BookAuthor4.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor4')])
        self.BookAuthor5.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor5')])
        self.BookPublisher.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookPublisher')])
        self.BookPubPlace.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookPubPlace')])
        self.BookYear.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookYear')]))
        
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
        
        self.ArchiveName.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveName')])
        self.ArchiveCollection.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveCollection')])
        self.ArchiveYear.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveYear')]))
        self.ArchiveMonth.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveMonth')]))
        self.ArchiveDay.WriteText(str(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveDay')]))
        self.ArchiveStack.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveStack')])
        self.ArchiveExpedientes.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveExpedientes')])
        
    def PopulateSourceEntryFields(self):
        self.BookPageNumbers.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('BookPageNumbers')])
        self.BookNotes.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('BookNotes')])
        
        self.ArticlePageNumbers.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArticlePageNumbers')])
        self.ArticleNotes.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArticleNotes')])
        
        self.ArchivePageNumbers.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchivePageNumbers')])
        self.ArchivePhotoReference.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchivePhotoReference')])
        self.ArchiveNotes.WriteText(self.SourceEntryFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchiveNotes')])
        
            
    def PopulateFields(self):
        self.DocumentType.SetStringSelection(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('DocumentType')])
        self.PopulateSourceFields()
        self.PopulateSourceEntryFields()
        
        
                
    def ClearFields(self):        
        self.SourceID = ''
        self.SourceFields = []
        self.SourceEntryID = ''
        self.SourceEntryFields = []
        for tupple in self.bookList:
            tupple[1].Clear()
        for tupple in self.articleList:
            tupple[1].Clear()
        for tupple in self.archiveList:
            tupple[1].Clear()
        
    def OnChangeType(self, evt):
        if self.DocumentType.GetValue() == self.initialType:
            self.SourceID = self.initialSourceID
        else:
            self.SourceID = ''
            
        self.ArrangeFields(self.DocumentType.GetSelection())
        self.SourceChanged = True
        
    def OnButtonClearFields(self, evt):
        documentType = self.DocumentType.GetSelection()
        self.ClearFields()
        self.ArrangeFields(documentType)
        self.SourceChanged = True
        
    def OnButtonSelectSource(self, evt):
        #Start Source List Window
        win = SourceListUI.SourceListCtrlFrame(self, self.DocumentType.GetSelection())
        win.Show(True)
        self.frame = win        
        evt.Skip()
        
    def SourceHasChanged(self, evt):
        self.SourceChanged = True
        
        