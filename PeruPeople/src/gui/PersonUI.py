import wx
import PeruConstants
from database import PersonDB

def getPersonInfo(personPage):
    return [str(personPage.PersonID),
            personPage.FirstName.GetValue(),
            personPage.LastName.GetValue(),
            personPage.Location.GetValue(),
            personPage.Ayllu.GetValue(),
            str(personPage.Region.GetValue()),
            str(personPage.Gender.GetValue()),
            str(personPage.Casta.GetValue()),
            str(personPage.Age.GetValue()),
            str(personPage.AgeRange.GetValue()),
            personPage.Profession.GetValue(),
            personPage.Occupation.GetValue(),
            str(personPage.ReligionCatholic.GetValue()),
            str(personPage.ReligionNative.GetValue()),
            str(personPage.ReligionOther.GetValue()),
            personPage.ReligionOtherText.GetValue(),
            personPage.Notes.GetValue(),
            str(personPage.TagForExample.GetValue())]
    
def savePerson(database, personPage):   
        return PersonDB.InsertUpdatePerson(database, getPersonInfo(personPage))

class PersonPanel(wx.Panel):
    def __init__(self, parent, PersonID):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)        
        
        space = 6
        
        if(PersonID > 0):
            self.PersonID = PersonID
            self.PersonFields = PersonDB.ReadPerson(PersonID)[1][0]
        else:
            PersonID = self.PersonID = ''
            self.PersonFields = self.PersonFields = []
        
        fieldList = self.fieldList = []

        FirstName = self.FirstName = wx.TextCtrl(self, size=(400,-1),name="First Name")
        fieldList.append((wx.StaticText(self, label="First Name :"), FirstName))
        
        LastName = self.LastName = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Last Name :"), LastName))
        
        Location = self.Location = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Location :"), Location))
        
        Ayllu = self.Ayllu = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Ayllu :"), Ayllu))
        
        Region = self.Region = wx.ComboBox(self, 500, PeruConstants.DEFAULT_REGION, (90, 50), (150, -1), PeruConstants.REGION_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        fieldList.append((wx.StaticText(self, label="Region :"), Region))
        
        Gender = self.Gender = wx.ComboBox(self, 500, PeruConstants.DEFAULT_GENDER, (90, 50), (50, -1), PeruConstants.GENDER_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        fieldList.append((wx.StaticText(self, label="Gender :"), Gender))
        
        Casta = self.Casta = wx.ComboBox(self, 500, PeruConstants.DEFAULT_CASTA, (90, 50), (150, -1), PeruConstants.CASTA_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        fieldList.append((wx.StaticText(self, label="Casta :"), Casta))
        
        Age = self.Age = wx.TextCtrl(self, size=(50,-1))
        fieldList.append((wx.StaticText(self, label="Age :"), Age))
        
        AgeRange = self.AgeRange = wx.ComboBox(self, 500, PeruConstants.AGE_RANGE_DEFAULT, (90, 50), (90, -1), PeruConstants.AGE_RANGE_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )
        fieldList.append((wx.StaticText(self, label="Age Range :"), AgeRange))
        
        Profession = self.Profession = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Profession/Skills :"), Profession))
        
        Occupation = self.Occupation = wx.TextCtrl(self, size=(400,-1))
        fieldList.append((wx.StaticText(self, label="Occupation/Role :"), Occupation))        
        
        ReligionCatholic = self.ReligionCatholic = wx.CheckBox(self, -1, "Catholic")
        ReligionNative = self.ReligionNative = wx.CheckBox(self, -1, "Native")
        ReligionOther = self.ReligionOther = wx.CheckBox(self, -1, "Other")
        ReligionOtherText = self.ReligionOtherText = wx.TextCtrl(self, size=(400,-1))
        ReligionSizer = wx.GridBagSizer(hgap=space, vgap=space)
        ReligionSizer.Add(ReligionCatholic, (0,0))
        ReligionSizer.Add(ReligionNative,   (0,1))
        ReligionSizer.Add(ReligionOther,    (0,2))
        ReligionSizer.Add(ReligionOtherText,(0,3))        
        fieldList.append((wx.StaticText(self, label="Religion :"), ReligionSizer))
        
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        fieldList.append((wx.StaticText(self, label="Notes :"), Notes))
        
        TagForExample = self.TagForExample = wx.CheckBox(self, -1, "Tag For Example")    
        
        self.Bind(wx.EVT_TEXT, self.EvtText, Age)

        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        for i in range(len(fieldList) - 1):                
            infoSizer.Add(fieldList[i][0],    (i+1,0))
            infoSizer.Add(fieldList[i][1],    (i+1,1))                
        
        #Add notes    
        infoSizer.Add(fieldList[len(fieldList)-1][0],     (len(fieldList),0))
        infoSizer.Add(fieldList[len(fieldList)-1][1],     (len(fieldList),1), (4,2), wx.EXPAND)
        
        infoSizer.Add(TagForExample, (len(fieldList)+4,0))
        
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        
        #Populate fields with content from current person
        if(PersonID != ''):
            self.PopulateFields()

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
            
    def PopulateFields(self):
        self.FirstName.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('FirstName')])
        self.LastName.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('LastName')])
        self.Location.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Location')])
        self.Ayllu.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Ayllu')])
        self.Region.SetStringSelection(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Region')])
        self.Gender.SetStringSelection(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Gender')])
        self.Casta.SetStringSelection(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Casta')])
        self.Age.WriteText(str(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Age')]))
        # Age range self populates
        self.Profession.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Profession')])
        self.Occupation.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Occupation')])
        self.ReligionCatholic.SetValue('True' == self.PersonFields[PeruConstants.PERSON_FIELDS.index('ReligionCatholic')])
        self.ReligionNative.SetValue('True' == self.PersonFields[PeruConstants.PERSON_FIELDS.index('ReligionNative')])
        self.ReligionOther.SetValue('True' == self.PersonFields[PeruConstants.PERSON_FIELDS.index('ReligionOther')])
        self.ReligionOtherText.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('ReligionOtherText')])
        self.Notes.WriteText(self.PersonFields[PeruConstants.PERSON_FIELDS.index('Notes')])
        self.TagForExample.SetValue('True' == self.PersonFields[PeruConstants.PERSON_FIELDS.index('TagForExample')])
            
        
