import wx
import PeruConstants
from database import MatrixDB

def getMatrixInfo(matrixPage):
    return [str(matrixPage.MatrixID),
            str(matrixPage.GetPage(0).Consulter.GetValue()),
            str(matrixPage.GetPage(0).Huaca.GetValue()),
            str(matrixPage.GetPage(0).Malqui.GetValue()),
            str(matrixPage.GetPage(0).Lightning.GetValue()),
            str(matrixPage.GetPage(0).Sun.GetValue()),
            str(matrixPage.GetPage(0).Capycocha.GetValue()),
            str(matrixPage.GetPage(0).OtherConsulter.GetValue()),
            matrixPage.GetPage(0).OtherConsulterText.GetValue(),
            str(matrixPage.GetPage(0).GuardianOf.GetValue()),
            matrixPage.GetPage(0).GuardianOfText.GetValue(),
            str(matrixPage.GetPage(0).Diviners.GetValue()),
            str(matrixPage.GetPage(0).Spiders.GetValue()),
            str(matrixPage.GetPage(0).Molle.GetValue()),
            str(matrixPage.GetPage(0).Love.GetValue()),
            str(matrixPage.GetPage(0).LostThings.GetValue()),
            str(matrixPage.GetPage(0).Mushrooms.GetValue()),
            str(matrixPage.GetPage(0).CuyExaminers.GetValue()),
            matrixPage.GetPage(0).PurposeText.GetValue(),
            str(matrixPage.GetPage(0).Curer.GetValue()),
            str(matrixPage.GetPage(0).Confessor.GetValue()),
            str(matrixPage.GetPage(0).Curandero.GetValue()),
            str(matrixPage.GetPage(0).HelperSacristan.GetValue()),
            str(matrixPage.GetPage(0).ChichaAsuacAccacMaker.GetValue()),
            str(matrixPage.GetPage(0).ChacraLandGuardian.GetValue()),
            str(matrixPage.GetPage(0).BloodsuckersDeathDealersCaptains.GetValue()),
            str(matrixPage.GetPage(0).Dogmatizer.GetValue()),
            str(matrixPage.GetPage(0).EmbustaroLiar.GetValue()),
            str(matrixPage.GetPage(0).Hecicero.GetValue()),
            str(matrixPage.GetPage(0).Brujo.GetValue()),
            str(matrixPage.GetPage(0).Sortilejo.GetValue()),
            str(matrixPage.GetPage(0).SacristanHelper.GetValue()),
            str(matrixPage.GetPage(0).ChichaMaker.GetValue()),
            str(matrixPage.GetPage(0).RelapserBackslider.GetValue()),
            matrixPage.GetPage(0).OtherChurchClassText.GetValue(),
            str(matrixPage.GetPage(0).YesTortured.GetValue()),
            str(matrixPage.GetPage(0).NoTortured.GetValue()),
            str(matrixPage.GetPage(0).UnableToDetermineTorture.GetValue()),
            str(matrixPage.GetPage(0).FamilySuccession.GetValue()),
            str(matrixPage.GetPage(0).Elected.GetValue()),
            str(matrixPage.GetPage(0).PersonalElection.GetValue()),
            str(matrixPage.GetPage(0).UnableToDetermineProf.GetValue()),
            str(matrixPage.GetPage(0).Blind.GetValue()),
            str(matrixPage.GetPage(0).OneEyed.GetValue()),
            str(matrixPage.GetPage(0).Lame.GetValue()),
            str(matrixPage.GetPage(0).Deaf.GetValue()),
            str(matrixPage.GetPage(0).Mute.GetValue()),
            str(matrixPage.GetPage(0).Crippled.GetValue()),
            str(matrixPage.GetPage(0).OtherCondition.GetValue()),
            matrixPage.GetPage(0).OtherConditionText.GetValue(),
            str(matrixPage.GetPage(0).YesDevil.GetValue()),
            str(matrixPage.GetPage(0).NoDevil.GetValue()),
            str(matrixPage.GetPage(0).UnableToDetermineDevil.GetValue()),
            str(matrixPage.GetPage(0).Whipped.GetValue()),
            str(matrixPage.GetPage(0).PublicService.GetValue()),
            str(matrixPage.GetPage(0).CutHair.GetValue()),
            str(matrixPage.GetPage(0).Executed.GetValue()),
            str(matrixPage.GetPage(0).Exiled.GetValue()),
            str(matrixPage.GetPage(0).OtherPunishment.GetValue()),
            matrixPage.GetPage(0).OtherPunishmentText.GetValue(),
            str(matrixPage.GetPage(0).Sacrifices.GetValue()),
            str(matrixPage.GetPage(0).Chants.GetValue()),
            str(matrixPage.GetPage(0).Incantations.GetValue()),
            str(matrixPage.GetPage(0).Song.GetValue()),
            str(matrixPage.GetPage(0).Dance.GetValue()),
            str(matrixPage.GetPage(0).Ritual.GetValue()),
            str(matrixPage.GetPage(0).Celebration.GetValue()),
            str(matrixPage.GetPage(0).OtherTechniques.GetValue()),
            matrixPage.GetPage(0).OtherTechniquesText.GetValue(),
            matrixPage.GetPage(0).NotesTechniquesText.GetValue(),
            matrixPage.GetPage(1).SpecialClothing.GetValue(),
            matrixPage.GetPage(2).Cosmology.GetValue(),
            matrixPage.GetPage(3).Ethnomedicine.GetValue(),
            matrixPage.GetPage(4).African.GetValue(),
            matrixPage.GetPage(5).GeneralNotes.GetValue()]
    
def saveMatrix(database, matrixPage):
        return MatrixDB.InsertUpdateMatrix(database, getMatrixInfo(matrixPage))

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
        
        Consulter                        = self.Consulter = wx.CheckBox(self, -1, "Consulter")
        Consulter.Font = boxfont
        Huaca                            = self.Huaca = wx.CheckBox(self, -1, "Huaca")
        Malqui                           = self.Malqui = wx.CheckBox(self, -1, "Malqui/Munaos")
        Lightning                        = self.Lightning = wx.CheckBox(self, -1, "Lightning")
        Sun                              = self.Sun = wx.CheckBox(self, -1, "Sun")
        Capycocha                        = self.Capycocha = wx.CheckBox(self, -1, "Capycocha")
        OtherConsulter                   = self.OtherConsulter = wx.CheckBox(self, -1, "Other")        
        OtherConsulterText               = self.OtherConsulterText = wx.TextCtrl(self, size=(150,-1),name="OtherConsulterText")
        GuardianOf                       = self.GuardianOf = wx.CheckBox(self, -1, "Guardian Of")
        GuardianOfText                   = self.GuardianOfText = wx.TextCtrl(self, size=(150,-1),name="GuardianOfText")
        
        Diviners                         = self.Diviners = wx.CheckBox(self, -1, "Diviners")
        Diviners.Font = boxfont
        Spiders                          = self.Spiders = wx.CheckBox(self, -1, "Spiders")
        Molle                            = self.Molle = wx.CheckBox(self, -1, "Molle")
        Love                             = self.Love = wx.CheckBox(self, -1, "Love")
        LostThings                       = self.LostThings = wx.CheckBox(self, -1, "Lost things")
        Mushrooms                        = self.Mushrooms = wx.CheckBox(self, -1, "Mushrooms")
        CuyExaminers                     = self.CuyExaminers = wx.CheckBox(self, -1, "Cuy Examiners")
        CuyExaminers.Font = boxfont
        labelPurpose = wx.StaticText(self, label="Purpose :")
        PurposeText                      = self.PurposeText = wx.TextCtrl(self, size=(150,-1),name="PurposeText")
        
        Curer                            = self.Curer = wx.CheckBox(self, -1, "Curer")
        Curer.Font = boxfont
        Confessor                        = self.Confessor = wx.CheckBox(self, -1, "Confessor")
        Confessor.Font = boxfont
        Curandero                        = self.Curandero = wx.CheckBox(self, -1, "Curandero/Curandera")
        Curandero.Font = boxfont
        HelperSacristan                  = self.HelperSacristan = wx.CheckBox(self, -1, "Helper/Sacristan")
        HelperSacristan.Font = boxfont
        ChichaAsuacAccacMaker            = self.ChichaAsuacAccacMaker = wx.CheckBox(self, -1, "Chicha/Asuac/ Accac Maker")
        ChichaAsuacAccacMaker.Font = boxfont
        ChacraLandGuardian               = self.ChacraLandGuardian = wx.CheckBox(self, -1, "Chacra/ Land Guardian ")
        ChacraLandGuardian.Font = boxfont
        BloodsuckersDeathDealersCaptains = self.BloodsuckersDeathDealersCaptains = wx.CheckBox(self, -1, "Bloodsuckers/ Death Dealers/ captains")
        BloodsuckersDeathDealersCaptains.Font = boxfont

        labelChurch = wx.StaticText(self, label="Church Classifications :")
        labelChurch.SetFont(largefont)
        
        Dogmatizer                       = self.Dogmatizer = wx.CheckBox(self, -1, "Dogmatizer")
        EmbustaroLiar                    = self.EmbustaroLiar = wx.CheckBox(self, -1, "Embustaro/a or Liar")
        Hecicero                         = self.Hecicero = wx.CheckBox(self, -1, "Hecicero/a")
        Brujo                            = self.Brujo = wx.CheckBox(self, -1, "Brujo/a")
        Sortilejo                        = self.Sortilejo = wx.CheckBox(self, -1, "Sortilejo")
        SacristanHelper                  = self.SacristanHelper = wx.CheckBox(self, -1, "Sacristan/ Helper")
        ChichaMaker                      = self.ChichaMaker = wx.CheckBox(self, -1, "Chicha Maker")
        RelapserBackslider               = self.RelapserBackslider = wx.CheckBox(self, -1, "Relapser/ Backslider")
        OtherChurchClass                 = self.OtherChurchClass = wx.CheckBox(self, -1, "Other")
        OtherChurchClassText             = self.OtherChurchClassText = wx.TextCtrl(self, size=(150,-1),name="OtherChurchClassText")
        
        

        labelTourtured = wx.StaticText(self, label="Tourtured :")
        labelTourtured.SetFont(largefont)
        
        YesTortured                      = self.YesTortured = wx.CheckBox(self, -1, "Yes")
        NoTortured                       = self.NoTortured = wx.CheckBox(self, -1, "No")
        UnableToDetermineTorture         = self.UnableToDetermineTorture = wx.CheckBox(self, -1, "Unable to Determine")
        

        labelProfession = wx.StaticText(self, label="Entered Profession :")
        labelProfession.SetFont(largefont)
        
        FamilySuccession                 = self.FamilySuccession = wx.CheckBox(self, -1, "Family Succession")
        Elected                          = self.Elected = wx.CheckBox(self, -1, "Elected")
        PersonalElection                 = self.PersonalElection = wx.CheckBox(self, -1, "Personal Election")
        UnableToDetermineProf            = self.UnableToDetermineProf = wx.CheckBox(self, -1, "Unable to Determine")
        

        labelCondition = wx.StaticText(self, label="Condition :")
        labelCondition.SetFont(largefont)
        
        Blind                            = self.Blind = wx.CheckBox(self, -1, "Blind")
        OneEyed                          = self.OneEyed = wx.CheckBox(self, -1, "One-Eyed")
        Lame                             = self.Lame = wx.CheckBox(self, -1, "Lame")
        Deaf                             = self.Deaf = wx.CheckBox(self, -1, "Deaf")
        Mute                             = self.Mute = wx.CheckBox(self, -1, "Mute")
        Crippled                         = self.Crippled = wx.CheckBox(self, -1, "Crippled")
        OtherCondition                   = self.OtherCondition = wx.CheckBox(self, -1, "Other")
        OtherConditionText               = self.OtherConditionText = wx.TextCtrl(self, size=(150,-1),name="OtherConditionText")
        

        labelDevil = wx.StaticText(self, label="Pact w/ the Devil or Demon :")
        labelDevil.SetFont(largefont)
        
        YesDevil                         = self.YesDevil = wx.CheckBox(self, -1, "Yes")
        NoDevil                          = self.NoDevil = wx.CheckBox(self, -1, "No")
        UnableToDetermineDevil           = self.UnableToDetermineDevil = wx.CheckBox(self, -1, "Unable to Determine")
        

        labelPunishment = wx.StaticText(self, label="Punishment :")
        labelPunishment.SetFont(largefont)
        
        Whipped                          = self.Whipped = wx.CheckBox(self, -1, "Whipped")
        PublicService                    = self.PublicService = wx.CheckBox(self, -1, "Public Service")
        CutHair                          = self.CutHair = wx.CheckBox(self, -1, "Cut Hair")
        Executed                         = self.Executed = wx.CheckBox(self, -1, "Executed")
        Exiled                           = self.Exiled = wx.CheckBox(self, -1, "Exiled")
        OtherPunishment                  = self.OtherPunishment = wx.CheckBox(self, -1, "Other Punishment")
        OtherPunishmentText              = self.OtherPunishmentText = wx.TextCtrl(self, size=(150,-1),name="OtherPunishmentText")
        

        labelTechniqes = wx.StaticText(self, label="Techniques/Methods :")
        labelTechniqes.SetFont(largefont)
        
        Sacrifices                       = self.Sacrifices = wx.CheckBox(self, -1, "Sacrifices")
        Chants                           = self.Chants = wx.CheckBox(self, -1, "Chants")
        Incantations                     = self.Incantations = wx.CheckBox(self, -1, "Incantations/prayers")
        Song                             = self.Song = wx.CheckBox(self, -1, "Song")
        Dance                            = self.Dance = wx.CheckBox(self, -1, "Dance")
        Ritual                           = self.Ritual = wx.CheckBox(self, -1, "Ritual")
        Celebration                      = self.Celebration = wx.CheckBox(self, -1, "Celebration")
        OtherTechniques                  = self.OtherTechniques = wx.CheckBox(self, -1, "Other")
        OtherTechniquesText              = self.OtherTechniquesText = wx.TextCtrl(self, size=(150,-1),name="OtherTechniquesText")
        NotesTechniquesLabel = wx.StaticText(self, label="Notes: ")
        NotesTechniquesText              = self.NotesTechniquesText = wx.TextCtrl(self, size=(150,-1),name="NotesTechniquesText")

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
        NotesTechniquesSizer.Add(NotesTechniquesLabel ,(0,0))
        NotesTechniquesSizer.Add(NotesTechniquesText  ,(0,1))
        infoSizer.Add(NotesTechniquesSizer            ,(9,16))   


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)

        self.SetSizer(sizer)
        
class SpecialClothingMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        SpecialClothing = self.SpecialClothing = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(SpecialClothing , 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
class CosmologyMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        Cosmology = self.Cosmology = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Cosmology , 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
class EthnomedicineMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        Ethnomedicine = self.Ethnomedicine = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Ethnomedicine , 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
class AfricanMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        African = self.African = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(African , 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
class GeneralNotesMatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        GeneralNotes = self.GeneralNotes = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(GeneralNotes, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)


class MatrixPanel(wx.Notebook):
    
    def __init__(self, parent, MatrixID):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
        
        if(MatrixID > 0):
            self.MatrixID = MatrixID
            self.MatrixFields = MatrixDB.ReadMatrix(MatrixID)[1][0]
        else:
            MatrixID = self.MatrixID = ''
            self.MatrixFields = self.MatrixFields = []

        self.AddPage(MainMatrixPanel(self), "Matrix")
        self.AddPage(SpecialClothingMatrixPanel(self), "Special Clothing Notes")
        self.AddPage(CosmologyMatrixPanel(self), "Cosmology Notes")
        self.AddPage(EthnomedicineMatrixPanel(self), "Ethnomedicine Notes")
        self.AddPage(AfricanMatrixPanel(self), "African Notes")
        self.AddPage(GeneralNotesMatrixPanel(self), "General Notes")
        
        #Populate fields with content from current person
        if(MatrixID != ''):
            self.PopulateFields()
        
    def PopulateFields(self):
        self.GetPage(0).Consulter.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('Consulter')])
        self.GetPage(0).Huaca.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterHuaca')])
        self.GetPage(0).Malqui.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterMalqui')])
        self.GetPage(0).Lightning.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterLightning')])
        self.GetPage(0).Sun.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterSun')])
        self.GetPage(0).Capycocha.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterCapycocha')])
        self.GetPage(0).OtherConsulter.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterOtherConsulter')])
        self.GetPage(0).OtherConsulterText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterOtherConsulterText')])                        
        self.GetPage(0).GuardianOf.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterGuardianOf')])
        self.GetPage(0).GuardianOfText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConsulterGuardianOfText')])
        self.GetPage(0).Diviners.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('Diviners')])
        self.GetPage(0).Spiders.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DivinersSpiders')])
        self.GetPage(0).Molle.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DivinersMolle')])
        self.GetPage(0).Love.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DivinersLove')])
        self.GetPage(0).LostThings.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DivinersLostThings')])
        self.GetPage(0).Mushrooms.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DivinersMushrooms')])
        self.GetPage(0).CuyExaminers.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DivinersCuyExaminers')])
        self.GetPage(0).PurposeText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DivinersPurposeText')])
        self.GetPage(0).Curer.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('Curer')])
        self.GetPage(0).Confessor.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('Confessor')])
        self.GetPage(0).Curandero.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('Curandero')])
        self.GetPage(0).HelperSacristan.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('HelperSacristan')])
        self.GetPage(0).ChichaAsuacAccacMaker.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChichaAsuacAccacMaker')])
        self.GetPage(0).ChacraLandGuardian.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChacraLandGuardian')])
        self.GetPage(0).BloodsuckersDeathDealersCaptains.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('BloodsuckersDeathDealersCaptains')])
        self.GetPage(0).Dogmatizer.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchDogmatizer')])
        self.GetPage(0).EmbustaroLiar.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchEmbustaroLiar')])
        self.GetPage(0).Hecicero.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchHecicero')])
        self.GetPage(0).Brujo.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchBrujo')])
        self.GetPage(0).Sortilejo.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchSortilejo')])
        self.GetPage(0).SacristanHelper.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchSacristanHelper')])
        self.GetPage(0).ChichaMaker.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchChichaMaker')])
        self.GetPage(0).RelapserBackslider.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchRelapserBackslider')])
        self.GetPage(0).OtherChurchClassText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ChurchOtherChurchClassText')])
        self.GetPage(0).YesTortured.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TorturedYesTortured')])
        self.GetPage(0).NoTortured.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TorturedNoTortured')])
        self.GetPage(0).UnableToDetermineTorture.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TorturedUnableToDetermineTorture')])
        self.GetPage(0).FamilySuccession.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ProfessionFamilySuccession')])
        self.GetPage(0).Elected.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ProfessionElected')])
        self.GetPage(0).PersonalElection.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ProfessionPersonalElection')])
        self.GetPage(0).UnableToDetermineProf.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ProfessionUnableToDetermineProf')])
        self.GetPage(0).Blind.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionBlind')])
        self.GetPage(0).OneEyed.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionOneEyed')])
        self.GetPage(0).Lame.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionLame')])
        self.GetPage(0).Deaf.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionDeaf')])
        self.GetPage(0).Mute.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionMute')])
        self.GetPage(0).Crippled.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionCrippled')])
        self.GetPage(0).OtherCondition.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionOtherCondition')])
        self.GetPage(0).OtherConditionText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('ConditionOtherConditionText')])
        self.GetPage(0).YesDevil.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DevilYesDevil')])
        self.GetPage(0).NoDevil.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DevilNoDevil')])
        self.GetPage(0).UnableToDetermineDevil.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('DevilUnableToDetermineDevil')])
        self.GetPage(0).Whipped.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('PunishmentWhipped')])
        self.GetPage(0).PublicService.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('PunishmentPublicService')])
        self.GetPage(0).CutHair.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('PunishmentCutHair')])
        self.GetPage(0).Executed.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('PunishmentExecuted')])
        self.GetPage(0).Exiled.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('PunishmentExiled')])
        self.GetPage(0).OtherPunishment.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('PunishmentOtherPunishment')])
        self.GetPage(0).OtherPunishmentText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('PunishmentOtherPunishmentText')])
        self.GetPage(0).Sacrifices.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesSacrifices')])
        self.GetPage(0).Chants.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesChants')])
        self.GetPage(0).Incantations.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesIncantations')])
        self.GetPage(0).Song.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesSong')])
        self.GetPage(0).Dance.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesDance')])
        self.GetPage(0).Ritual.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesRitual')])
        self.GetPage(0).Celebration.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesCelebration')])
        self.GetPage(0).OtherTechniques.SetValue('True' == self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesOtherTechniques')])
        self.GetPage(0).OtherTechniquesText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesOtherTechniquesText')])
        self.GetPage(0).NotesTechniquesText.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('TechniquesNotesTechniquesText')])
        self.GetPage(1).SpecialClothing.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('SpecialClothing')])
        self.GetPage(2).Cosmology.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('Cosmology')])
        self.GetPage(3).Ethnomedicine.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('Ethnomedicine')])
        self.GetPage(4).African.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('African')])
        self.GetPage(5).GeneralNotes.WriteText(self.MatrixFields[PeruConstants.MATRIX_FIELDS.index('GeneralNotes')])
