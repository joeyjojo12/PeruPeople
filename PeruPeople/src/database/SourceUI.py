import wx
import PeruConstants


def getSourceInfo(sourcePage):    
    return [str(sourcePage.SourceID),
            str(sourcePage.Type.GetValue()),
            str(sourcePage.Stack.GetValue()),
            str(sourcePage.Citation.GetValue()),
            str(sourcePage.Archive.GetValue()),
            str(sourcePage.PageNumbers.GetValue()),
            str(sourcePage.Author.GetValue()),
            str(sourcePage.DocNameTitle.GetValue()),
            str(sourcePage.PubPlace.GetValue()),
            str(sourcePage.Year.GetValue()),
            str(sourcePage.ReferencedByFirst.GetValue()),
            str(sourcePage.ReferencedByLast.GetValue()),
            str(sourcePage.Notes.GetValue())]
    
def saveSource(sourcePage):
        return SourceDB.InsertUpdateSource(getSourceInfo(sourcePage))




class SourcePanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        SourceID = self.SourceID  = ''
        
        fieldList = []

        Type = self.Type = wx.ComboBox(self, 500, PeruConstants.DEFAULT_DOCUMENT, (90, 50), (150, -1), PeruConstants.DOCUMENT_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        fieldList.append((wx.StaticText(self, label="Type :"), Type))
        
        Stack = self.Stack = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Stack :"), Stack ))

        Citation = self.Stack = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Citation :"), Citation))

        Archive = self.Stack = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Archive :"), Archive))

        PageNumbers = self.PageNumbers = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Page Numbers :"), PageNumbers))

        Author = self.Author = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Author :"), Author))

        DocNameTitle = self.DocNameTitle = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Document Name :"), DocNameTitle))

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

        self.SetSizer(sizer)





