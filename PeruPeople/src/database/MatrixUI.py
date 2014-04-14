import wx
import PeruConstants

class MainMatrixPanel(wx.ScrolledWindow):
    def __init__(self, parent):

        wx.ScrolledWindow.__init__(self, parent=parent, id=wx.ID_ANY)

        self.lines = []
        self.maxWidth  = 1000
        self.maxHeight = 1000
        self.x = self.y = 0
        self.curLine = []
        self.drawing = False

        self.SetVirtualSize((self.maxWidth, self.maxHeight))
        self.SetScrollRate(20,20)
        
        
        largefont = wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD)
        boxfont = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD)

        labelMinister = wx.StaticText(self, label="Type of Minister :")
        labelMinister.SetFont(largefont)
        
        Consulter                        = self.societal = wx.CheckBox(self, -1, "Consulter")
        Consulter.Font = boxfont
        Huaca                            = self.societal = wx.CheckBox(self, -1, "Huaca")
        Malqui                           = self.societal = wx.CheckBox(self, -1, "Malqui/Munaos")
        Lightning                        = self.societal = wx.CheckBox(self, -1, "Lightning")
        Sun                              = self.Societal = wx.CheckBox(self, -1, "Sun")
        Capycocha                        = self.Societal = wx.CheckBox(self, -1, "Capycocha")
        OtherConsulter                   = self.Societal = wx.CheckBox(self, -1, "Other")        
        OtherConsulterText               = wx.TextCtrl(self, size=(150,-1),name="OtherConsulterText")
        GuardianOf                       = self.Societal = wx.CheckBox(self, -1, "Guardian Of")
        GuardianOfText                   = wx.TextCtrl(self, size=(150,-1),name="GuardianOfText")
        
        Diviners                         = self.societal = wx.CheckBox(self, -1, "Diviners")
        Diviners.Font = boxfont
        Spiders                          = self.societal = wx.CheckBox(self, -1, "Spiders")
        Molle                            = self.societal = wx.CheckBox(self, -1, "Molle")
        Love                             = self.societal = wx.CheckBox(self, -1, "Love")
        LostThings                       = self.Societal = wx.CheckBox(self, -1, "Lost things")
        Mushrooms                        = self.Societal = wx.CheckBox(self, -1, "Mushrooms")
        CuyExaminers                     = self.societal = wx.CheckBox(self, -1, "Cuy Examiners")
        CuyExaminers.Font = boxfont
        labelPurpose = wx.StaticText(self, label="Purpose :")
        PurposeText                   = wx.TextCtrl(self, size=(150,-1),name="PurposeText")
        
        Curer                            = self.societal = wx.CheckBox(self, -1, "Curer")
        Curer.Font = boxfont
        Confessor                        = self.societal = wx.CheckBox(self, -1, "Confessor")
        Confessor.Font = boxfont
        Curandero                        = self.societal = wx.CheckBox(self, -1, "Curandero/Curandera")
        Curandero.Font = boxfont
        HelperSacristan                  = self.societal = wx.CheckBox(self, -1, "Helper/Sacristan")
        HelperSacristan.Font = boxfont
        ChichaAsuacAccacMaker            = self.societal = wx.CheckBox(self, -1, "Chicha/Asuac/ Accac Maker")
        ChichaAsuacAccacMaker.Font = boxfont
        ChacraLandGuardian               = self.societal = wx.CheckBox(self, -1, "Chacra/ Land Guardian ")
        ChacraLandGuardian.Font = boxfont
        BloodsuckersDeathDealersCaptains = self.societal = wx.CheckBox(self, -1, "Bloodsuckers/ Death Dealers/ captains")
        BloodsuckersDeathDealersCaptains.Font = boxfont

        labelChurch = wx.StaticText(self, label="Church Classifications :")
        labelChurch.SetFont(largefont)
        
        Dogmatizer                       = self.societal = wx.CheckBox(self, -1, "Dogmatizer")
        EmbustaroLiar                    = self.societal = wx.CheckBox(self, -1, "Embustaro/a or Liar")
        Hecicero                         = self.societal = wx.CheckBox(self, -1, "Hecicero/a")
        Brujo                            = self.societal = wx.CheckBox(self, -1, "Brujo/a")
        Sortilejo                        = self.societal = wx.CheckBox(self, -1, "Sortilejo")
        SacristanHelper                  = self.societal = wx.CheckBox(self, -1, "Sacristan/ Helper")
        ChichaMaker                      = self.societal = wx.CheckBox(self, -1, "Chicha Maker")
        RelapserBackslider               = self.societal = wx.CheckBox(self, -1, "Relapser/ Backslider")
        OtherChurchClass                 = self.societal = wx.CheckBox(self, -1, "Other")
        OtherChurchClassText             = wx.TextCtrl(self, size=(150,-1),name="OtherChurchClassText")
        
        

        labelTourtured = wx.StaticText(self, label="Tourtured :")
        labelTourtured.SetFont(largefont)
        
        YesTortured                      = self.societal = wx.CheckBox(self, -1, "Yes")
        NoTortured                       = self.societal = wx.CheckBox(self, -1, "No")
        UnableToDetermineTorture         = self.societal = wx.CheckBox(self, -1, "Unable to Determine")
        

        labelProfession = wx.StaticText(self, label="Entered Profession :")
        labelProfession.SetFont(largefont)
        
        FamilySuccession                 = self.societal = wx.CheckBox(self, -1, "Family Succession")
        Elected                          = self.societal = wx.CheckBox(self, -1, "Elected")
        PersonalElection                 = self.societal = wx.CheckBox(self, -1, "Personal Election")
        UnableToDetermineProf            = self.societal = wx.CheckBox(self, -1, "Unable to Determine")
        

        labelCondition = wx.StaticText(self, label="Condition :")
        labelCondition.SetFont(largefont)
        
        Blind                            = self.societal = wx.CheckBox(self, -1, "Blind")
        OneEyed                          = self.societal = wx.CheckBox(self, -1, "One-Eyed")
        Lame                             = self.societal = wx.CheckBox(self, -1, "Lame")
        Deaf                             = self.societal = wx.CheckBox(self, -1, "Deaf")
        Mute                             = self.societal = wx.CheckBox(self, -1, "Mute")
        Crippled                         = self.societal = wx.CheckBox(self, -1, "Crippled")
        OtherCondition                   = self.societal = wx.CheckBox(self, -1, "Other")
        OtherConditionText               = wx.TextCtrl(self, size=(150,-1),name="OtherConditionText")
        

        labelDevil = wx.StaticText(self, label="Pact w/ the Devil or Demon :")
        labelDevil.SetFont(largefont)
        
        YesDevil                         = self.societal = wx.CheckBox(self, -1, "Yes")
        NoDevil                          = self.societal = wx.CheckBox(self, -1, "No")
        UnableToDetermineDevil           = self.societal = wx.CheckBox(self, -1, "Unable to Determine")
        

        labelPunishment = wx.StaticText(self, label="Punishment :")
        labelPunishment.SetFont(largefont)
        
        Whipped                          = self.societal = wx.CheckBox(self, -1, "Whipped")
        PublicService                    = self.societal = wx.CheckBox(self, -1, "Public Service")
        CutHair                          = self.societal = wx.CheckBox(self, -1, "Cut Hair")
        Executed                         = self.societal = wx.CheckBox(self, -1, "Executed")
        Exiled                           = self.societal = wx.CheckBox(self, -1, "Exiled")
        OtherPunishment                  = self.societal = wx.CheckBox(self, -1, "Other Punishment")
        OtherPunishmentText              = wx.TextCtrl(self, size=(150,-1),name="OtherPunishmentText")
        

        labelTechniqes = wx.StaticText(self, label="Techniques/Methods :")
        labelTechniqes.SetFont(largefont)
        
        Sacrifices                       = self.societal = wx.CheckBox(self, -1, "Sacrifices")
        Chants                           = self.societal = wx.CheckBox(self, -1, "Chants")
        Incantations                     = self.societal = wx.CheckBox(self, -1, "Incantations/prayers")
        Song                             = self.societal = wx.CheckBox(self, -1, "Song")
        Dance                            = self.societal = wx.CheckBox(self, -1, "Dance")
        Ritual                           = self.societal = wx.CheckBox(self, -1, "Ritual")
        Celebration                      = self.societal = wx.CheckBox(self, -1, "Celebration")
        OtherTechniques                  = self.societal = wx.CheckBox(self, -1, "Other")
        OtherTechniquesText              = wx.TextCtrl(self, size=(150,-1),name="OtherTechniquesText")
        NotesTechniques                  = self.societal = wx.CheckBox(self, -1, "Notes")
        NotesTechniquesText              = wx.TextCtrl(self, size=(150,-1),name="NotesTechniquesText")

        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        infoSizer.Add(labelMinister                   ,(0,0))
        infoSizer.Add(Consulter                       ,(1,0))
        infoSizer.Add(Huaca                           ,(2,0))
        infoSizer.Add(Malqui                          ,(3,0))
        infoSizer.Add(Lightning                       ,(4,0))
        infoSizer.Add(Sun                             ,(5,0))
        infoSizer.Add(Capycocha                       ,(6,0))
        otherConsulterSizer = wx.GridBagSizer(hgap=space, vgap=space)
        otherConsulterSizer.Add(OtherConsulter        ,(0,0))
        otherConsulterSizer.Add(OtherConsulterText    ,(0,1))
        infoSizer.Add(otherConsulterSizer             ,(7,0))
        GuardianOfSizer = wx.GridBagSizer(hgap=space, vgap=space)
        GuardianOfSizer.Add(GuardianOf                ,(0,0))
        GuardianOfSizer.Add(GuardianOfText            ,(0,1))
        infoSizer.Add(GuardianOfSizer                 ,(8,0))
        
        infoSizer.Add(Diviners                        ,(10,0))        
        infoSizer.Add(Spiders                         ,(11,0))
        infoSizer.Add(Molle                           ,(12,0))
        infoSizer.Add(Love                            ,(13,0))
        infoSizer.Add(LostThings                      ,(14,0))
        infoSizer.Add(Mushrooms                       ,(15,0))
        
        infoSizer.Add(CuyExaminers                    ,(17,0))
        PurposeSizer = wx.GridBagSizer(hgap=space, vgap=space)
        PurposeSizer.Add(labelPurpose                 ,(0,0))
        PurposeSizer.Add(PurposeText                  ,(0,1))
        infoSizer.Add(PurposeSizer                    ,(18,0))
                
        infoSizer.Add(Curer                           ,(20,0))        
        infoSizer.Add(Confessor                       ,(21,0))        
        infoSizer.Add(Curandero                       ,(22,0))        
        infoSizer.Add(HelperSacristan                 ,(23,0))        
        infoSizer.Add(ChichaAsuacAccacMaker           ,(24,0))        
        infoSizer.Add(ChacraLandGuardian              ,(25,0))        
        infoSizer.Add(BloodsuckersDeathDealersCaptains,(26,0))    

        infoSizer.Add(labelChurch                     ,(0,4))
        infoSizer.Add(Dogmatizer                      ,(1,4))
        infoSizer.Add(EmbustaroLiar                   ,(2,4))
        infoSizer.Add(Hecicero                        ,(3,4))
        infoSizer.Add(Brujo                           ,(4,4))
        infoSizer.Add(Sortilejo                       ,(5,4))
        infoSizer.Add(SacristanHelper                 ,(6,4))
        infoSizer.Add(ChichaMaker                     ,(7,4))
        infoSizer.Add(RelapserBackslider              ,(8,4))
        OtherChurchClassSizer = wx.GridBagSizer(hgap=space, vgap=space)
        OtherChurchClassSizer.Add(OtherChurchClass    ,(0,0))
        OtherChurchClassSizer.Add(OtherChurchClassText,(0,1))
        infoSizer.Add(OtherChurchClassSizer           ,(9,4))

        infoSizer.Add(labelTourtured                  ,(11,4))
        infoSizer.Add(YesTortured                     ,(12,4))
        infoSizer.Add(NoTortured                      ,(13,4))
        infoSizer.Add(UnableToDetermineTorture        ,(14,4))
        

        infoSizer.Add(labelProfession                 ,(0,8))
        infoSizer.Add(FamilySuccession                ,(1,8))
        infoSizer.Add(Elected                         ,(2,8))
        infoSizer.Add(PersonalElection                ,(3,8))
        infoSizer.Add(UnableToDetermineProf           ,(4,8))


        infoSizer.Add(labelCondition                  ,(6,8))
        infoSizer.Add(Blind                           ,(7,8))
        infoSizer.Add(OneEyed                         ,(8,8))
        infoSizer.Add(Lame                            ,(9,8))
        infoSizer.Add(Deaf                            ,(10,8))
        infoSizer.Add(Mute                            ,(11,8))
        infoSizer.Add(Crippled                        ,(12,8))
        OtherConditionSizer = wx.GridBagSizer(hgap=space, vgap=space)
        OtherConditionSizer.Add(OtherCondition        ,(0,0))
        OtherConditionSizer.Add(OtherConditionText    ,(0,1))
        infoSizer.Add(OtherConditionSizer             ,(13,8))
        
        
        infoSizer.Add(labelDevil                      ,(0,12))
        infoSizer.Add(YesDevil                        ,(1,12))
        infoSizer.Add(NoDevil                         ,(2,12))
        infoSizer.Add(UnableToDetermineDevil          ,(3,12))


        infoSizer.Add(labelPunishment                 ,(5,12))
        infoSizer.Add(Whipped                         ,(6,12))
        infoSizer.Add(PublicService                   ,(7,12))
        infoSizer.Add(CutHair                         ,(8,12))
        infoSizer.Add(Executed                        ,(9,12))
        infoSizer.Add(Exiled                          ,(10,12))
        OtherPunishmentSizer = wx.GridBagSizer(hgap=space, vgap=space)
        OtherPunishmentSizer.Add(OtherPunishment      ,(0,0))
        OtherPunishmentSizer.Add(OtherPunishmentText  ,(0,1))
        infoSizer.Add(OtherPunishmentSizer            ,(11,12))
         
        infoSizer.Add(labelTechniqes                  ,(0,16))
        infoSizer.Add(Sacrifices                      ,(1,16))
        infoSizer.Add(Chants                          ,(2,16))
        infoSizer.Add(Incantations                    ,(3,16))
        infoSizer.Add(Song                            ,(4,16))
        infoSizer.Add(Dance                           ,(5,16))
        infoSizer.Add(Ritual                          ,(6,16))
        infoSizer.Add(Celebration                     ,(7,16))
        OtherTechniquesSizer = wx.GridBagSizer(hgap=space, vgap=space)
        OtherTechniquesSizer.Add(OtherTechniques      ,(0,0))
        OtherTechniquesSizer.Add(OtherTechniquesText  ,(0,1))
        infoSizer.Add(OtherTechniquesSizer            ,(8,16))
        NotesTechniquesSizer = wx.GridBagSizer(hgap=space, vgap=space)
        NotesTechniquesSizer.Add(NotesTechniques      ,(0,0))
        NotesTechniquesSizer.Add(NotesTechniquesText  ,(0,1))
        infoSizer.Add(NotesTechniquesSizer            ,(9,16))   


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)

        self.SetSizer(sizer)
        
class SpecialClothingMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        Summary = self.Summary = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Summary, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
class CosmologyMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        Summary = self.Summary = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Summary, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
class EthnomedicineMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        Summary = self.Summary = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Summary, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
class GeneralNotesMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        Summary = self.Summary = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Summary, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)


class MatrixPanel(wx.Notebook):
    
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        self.AddPage(MainMatrixPanel(self), "Matrix")
        self.AddPage(SpecialClothingMatrixPanel(self), "Special Clothing Notes")
        self.AddPage(CosmologyMatrixPanel(self), "Cosmology Notes")
        self.AddPage(EthnomedicineMatrixPanel(self), "Ethnomedicine Notes")
        self.AddPage(GeneralNotesMatrixPanel(self), "General Notes")