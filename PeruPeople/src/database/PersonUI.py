import wx
import PeruConstants

class PersonPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        label1 = wx.StaticText(self, label="First Name :")
        FirstName = self.FirstName = wx.TextCtrl(self, size=(400,-1),name="First Name")
        label2 = wx.StaticText(self, label="Last Name :")
        LastName = self.LastName = wx.TextCtrl(self, size=(400,-1))
        label3 = wx.StaticText(self, label="Location :")
        Location = self.Location = wx.TextCtrl(self, size=(400,-1))
        label4 = wx.StaticText(self, label="Region :")
        Region = self.Region = wx.ComboBox(self, 500, PeruConstants.DEFAULT_REGION, (90, 50), (150, -1), PeruConstants.REGION_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label5 = wx.StaticText(self, label="Gender :")
        Gender = self.Gender = wx.ComboBox(self, 500, PeruConstants.DEFAULT_GENDER, (90, 50), (50, -1), PeruConstants.GENDER_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label6 = wx.StaticText(self, label="Age :")
        Age = self.Age = wx.TextCtrl(self, size=(50,-1))
        label7 = wx.StaticText(self, label="Age Range :")
        AgeRange = self.AgeRange = wx.ComboBox(self, 500, PeruConstants.AGE_RANGE_DEFAULT, (90, 50), (90, -1), PeruConstants.AGE_RANGE_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        label8 = wx.StaticText(self, label="Religion :")
        Religion = self.Religion = wx.TextCtrl(self, value="Catholic", size=(400,-1))
        label9 = wx.StaticText(self, label="Notes :")
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)        
        
        self.Bind(wx.EVT_TEXT, self.EvtText, Age)

        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        infoSizer.Add(label1,   (1,0))
        infoSizer.Add(FirstName,(1,1))
        infoSizer.Add(label2,   (2,0))
        infoSizer.Add(LastName, (2,1))
        infoSizer.Add(label3,   (3,0))
        infoSizer.Add(Location, (3,1))
        infoSizer.Add(label4,   (4,0))
        infoSizer.Add(Region,   (4,1))
        infoSizer.Add(label5,   (5,0))
        infoSizer.Add(Gender,   (5,1))
        infoSizer.Add(label6,   (6,0))
        infoSizer.Add(Age,      (6,1))
        infoSizer.Add(label7,   (7,0))
        infoSizer.Add(AgeRange, (7,1))
        infoSizer.Add(label8,   (8,0))
        infoSizer.Add(Religion, (8,1))
        infoSizer.Add(label9,   (9,0))
        infoSizer.Add(Notes,    (9,1), (4,2), wx.EXPAND)
        
        
        
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.savePersonButton = wx.Button(self, -1, "Save Person")
        self.readPersonButton = wx.Button(self, -1, "Read Person")        
        self.buttonSizer.Add(self.savePersonButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.readPersonButton, 0, wx.ALIGN_RIGHT)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        sizer.Add(self.buttonSizer, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizer)
        
    def EvtText(self, event):
        if event.GetString() == "":
            self.AgeRange.SetSelection(0)
            return
        
        age = int(event.GetString())
        if age > 99:
            self.AgeRange.SetSelection(10)
        else:
            self.AgeRange.SetSelection(age/10)