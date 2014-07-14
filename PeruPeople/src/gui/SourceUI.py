import wx
import PeruConstants
from database import SourceDB, SourceEntryDB


def getSourceInfo(sourcePage):
    return [str(sourcePage.SourceID),
            str(sourcePage.DocumentType.GetValue()),
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
        

        Type = self.DocumentType = wx.ComboBox(self, 500, PeruConstants.DEFAULT_DOCUMENT, (90, 50), (150, -1), PeruConstants.DOCUMENT_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
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
        BookPageNumbers = self.BookPageNumbers = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
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
        ArticlePageNumbers = self.ArticlePageNumbers = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
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
        ArchivePageNumbers = self.ArchivePageNumbers = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        archiveList.append((wx.StaticText(self, label="Page Numbers :"), ArchivePageNumbers))
        ArchiveNotes = self.ArchiveNotes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        archiveList.append((wx.StaticText(self, label="Notes :"), ArchiveNotes))
        ArchivePhotoReference = self.ArchivePhotoReference = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        archiveList.append((wx.StaticText(self, label="Photo Reference(s) :"), ArchivePhotoReference))
        
        sourceLists = [bookList, articleList, archiveList]
       
        space = 6
        infoSizer = self.infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
       
        #Initially set document type as archive
        self.ArrangeFields(PeruConstants.DEFAULT_DOCUMENT)
            
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
        self.DocumentType.SetStringSelection(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('DocumentType')])
        self.BookTitle.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookTitle')])
        self.BookAuthor1.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor1')])
        self.BookAuthor2.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor2')])
        self.BookAuthor3.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor3')])
        self.BookAuthor4.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor4')])
        self.BookAuthor5.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookAuthor5')])
        self.BookPublisher.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookPublisher')])
        self.BookPubPlace.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookPubPlace')])
        self.BookYear.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('BookYear')])
        self.BookPageNumbers.WriteText(self.SourceFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('BookPageNumbers')])
        self.BookNotes.WriteText(self.SourceFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('BookNotes')])
        self.ArticleTitle.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleTitle')])
        self.ArticleAuthor2.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor1')])
        self.ArticleAuthor2.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor2')])
        self.ArticleAuthor3.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor3')])
        self.ArticleAuthor4.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor4')])
        self.ArticleAuthor5.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleAuthor5')])
        self.ArticlePublication.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticlePublication')])
        self.ArticleYear.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleYear')])
        self.ArticleVolume.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleVolume')])
        self.ArticleIssue.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArticleIssue')])
        self.ArticlePageNumbers.WriteText(self.SourceFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArticlePageNumbers')])
        self.ArticleNotes.WriteText(self.SourceFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArticleNotes')])
        self.ArchiveName.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveName')])
        self.ArchiveCollection.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveCollection')])
        self.ArchiveYear.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveYear')])
        self.ArchiveMonth.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveMonth')])
        self.ArchiveDay.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveDay')])
        self.ArchiveStackWriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveStack')])
        self.ArchiveExpedientes.WriteText(self.SourceFields[PeruConstants.SOURCE_FIELDS.index('ArchiveExpedientes')])
        self.ArchivePageNumbers.WriteText(self.SourceFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchivePageNumbers')])
        self.ArchiveNotes.WriteText(self.SourceFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchiveNotes')])
        self.ArchivePhotoReference.WriteText(self.SourceFields[PeruConstants.SOURCE_ENTRY_FIELDS.index('ArchivePhotoReference')])
        
    def OnChangeType(self, evt):
        self.ArrangeFields(self.Type.GetSelection())
        
        