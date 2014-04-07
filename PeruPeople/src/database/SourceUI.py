import wx
import PeruConstants

class SourcePanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        label1 = wx.StaticText(self, label="Type :")
        Type = self.Type = wx.ComboBox(self, 500, PeruConstants.DEFAULT_DOCUMENT, (90, 50), (150, -1), PeruConstants.DOCUMENT_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label2 = wx.StaticText(self, label="Stack :")
        Stack = self.Stack = wx.TextCtrl(self, size=(400,-1))
        label3 = wx.StaticText(self, label="Page Numbers :")
        PageNumbers = self.PageNumbers = wx.TextCtrl(self, size=(400,-1))
        label4 = wx.StaticText(self, label="Author :")
        Author = self.Author = wx.TextCtrl(self, size=(400,-1))
        label5 = wx.StaticText(self, label="Document Name :")
        DocNameTitle = self.DocNameTitle = wx.TextCtrl(self, size=(400,-1))
        label6 = wx.StaticText(self, label="Type :")
        Publisher = self.Publisher = wx.TextCtrl(self, size=(400,-1))
        label7 = wx.StaticText(self, label="Place of Publication :")
        PubPlace = self.PubPlace = wx.TextCtrl(self, size=(400,-1))
        label8 = wx.StaticText(self, label="Year :")
        Year = self.Year = wx.TextCtrl(self, size=(100,-1))
        label9 = wx.StaticText(self, label="Referenced By First Name :")
        ReferencedByFirst = self.ReferencedByFirst = wx.TextCtrl(self, size=(400,-1))
        label10 = wx.StaticText(self, label="Referenced By Last Name :")
        ReferencedByLast = self.ReferencedByLast = wx.TextCtrl(self, size=(400,-1))
        label11 = wx.StaticText(self, label="Notes :")
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)        
        
        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        infoSizer.Add(label1,            (1,0))
        infoSizer.Add(Type,              (1,1))
        infoSizer.Add(label2,            (2,0))
        infoSizer.Add(Stack,             (2,1))
        infoSizer.Add(label3,            (3,0))
        infoSizer.Add(PageNumbers,       (3,1))
        infoSizer.Add(label4,            (4,0))
        infoSizer.Add(Author,            (4,1))
        infoSizer.Add(label5,            (5,0))
        infoSizer.Add(DocNameTitle,      (5,1))
        infoSizer.Add(label6,            (6,0))
        infoSizer.Add(Publisher,         (6,1))
        infoSizer.Add(label7,            (7,0))
        infoSizer.Add(PubPlace,          (7,1))
        infoSizer.Add(label8,            (8,0))
        infoSizer.Add(Year,              (8,1))
        infoSizer.Add(label9,            (9,0))
        infoSizer.Add(ReferencedByFirst, (9,1))
        infoSizer.Add(label10,           (10,0))
        infoSizer.Add(ReferencedByLast,  (10,1))
        infoSizer.Add(label11,           (11,0))
        infoSizer.Add(Notes,             (11,1), (4,2), wx.EXPAND)
        
        
        
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.savePersonButton = wx.Button(self, -1, "Save Person")
        self.readPersonButton = wx.Button(self, -1, "Read Person")        
        self.buttonSizer.Add(self.savePersonButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.readPersonButton, 0, wx.ALIGN_RIGHT)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        sizer.Add(self.buttonSizer, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizer)
