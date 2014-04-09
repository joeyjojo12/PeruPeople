import wx
import PeruConstants

class MatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        
        largefont = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)

        labelMinister = wx.StaticText(self, label="Type of Minister :")
        labelMinister.SetFont(largefont)
        
        Consulter                        = self.societal = wx.CheckBox(self, -1, "Consulter")
        Huaca                            = self.societal = wx.CheckBox(self, -1, "Huaca")
        Malqui                           = self.societal = wx.CheckBox(self, -1, "Malqui/Munaos")
        Lightning                        = self.societal = wx.CheckBox(self, -1, "Lightning")
        Sun                              = self.Societal = wx.CheckBox(self, -1, "Sun")
        Capycocha                        = self.Societal = wx.CheckBox(self, -1, "Capycocha")
        OtherConsulter                   = self.Societal = wx.CheckBox(self, -1, "Other")
        Diviners                         = self.societal = wx.CheckBox(self, -1, "Diviners")
        Spiders                          = self.societal = wx.CheckBox(self, -1, "Spiders")
        Molle                            = self.societal = wx.CheckBox(self, -1, "Molle")
        Love                             = self.societal = wx.CheckBox(self, -1, "Love")
        LostThings                       = self.Societal = wx.CheckBox(self, -1, "Lost things")
        Mushrooms                        = self.Societal = wx.CheckBox(self, -1, "Mushrooms")
        CuyExaminers                     = self.societal = wx.CheckBox(self, -1, "Cuy Examiners")
        Purpose                          = self.societal = wx.CheckBox(self, -1, "Purpose")
        Curer                            = self.societal = wx.CheckBox(self, -1, "Curer")
        Confessor                        = self.societal = wx.CheckBox(self, -1, "Confessor")
        Curandero                        = self.societal = wx.CheckBox(self, -1, "Curandero/Curandera")
        HelperSacristan                  = self.societal = wx.CheckBox(self, -1, "Helper/Sacristan")
        ChichaAsuacAccacMaker            = self.societal = wx.CheckBox(self, -1, "Chicha/Asuac/ Accac Maker")
        ChacraLandGuardian               = self.societal = wx.CheckBox(self, -1, "Chacra/ Land Guardian ")
        BloodsuckersDeathDealersCaptains = self.societal = wx.CheckBox(self, -1, "Bloodsuckers/ Death Dealers/ captains")

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
        NotesTechniques                  = self.societal = wx.CheckBox(self, -1, "Notes")
#        
#        labelSpecialClothingNotes = wx.StaticText(self, label="Techniques/Methods :")
#        labelSpecialClothingNotes.SetFont(largefont)
#        
#        labelCosmologyNotes = wx.StaticText(self, label="Techniques/Methods :")
#        labelCosmologyNotes.SetFont(largefont)
#        
#        labelEthnomedicineNotes = wx.StaticText(self, label="Techniques/Methods :")
#        labelEthnomedicineNotes.SetFont(largefont)
#        
#        Tag                  = self.societal = wx.CheckBox(self, -1, "Tag individual for example")
        
        

        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        infoSizer.Add(labelMinister                   ,(0,0))
        infoSizer.Add(Consulter                       ,(1,0))
        infoSizer.Add(Huaca                           ,(2,0))
        infoSizer.Add(Malqui                          ,(3,0))
        infoSizer.Add(Lightning                       ,(4,0))
        infoSizer.Add(Sun                             ,(5,0))
        infoSizer.Add(Capycocha                       ,(6,0))
        infoSizer.Add(OtherConsulter                  ,(7,0))
        infoSizer.Add(Diviners                        ,(9,0))        
        infoSizer.Add(Spiders                         ,(10,0))
        infoSizer.Add(Molle                           ,(11,0))
        infoSizer.Add(Love                            ,(12,0))
        infoSizer.Add(LostThings                      ,(13,0))
        infoSizer.Add(Mushrooms                       ,(14,0))
        infoSizer.Add(CuyExaminers                    ,(16,0))        
        infoSizer.Add(Purpose                         ,(17,0))        
        infoSizer.Add(Curer                           ,(2,2))        
        infoSizer.Add(Confessor                       ,(4,2))        
        infoSizer.Add(Curandero                       ,(6,2))        
        infoSizer.Add(HelperSacristan                 ,(8,2))        
        infoSizer.Add(ChichaAsuacAccacMaker           ,(10,2))        
        infoSizer.Add(ChacraLandGuardian              ,(12,2))        
        infoSizer.Add(BloodsuckersDeathDealersCaptains,(14,2))    
         
        infoSizer.Add(labelTechniqes                  ,(20,0))
        infoSizer.Add(Sacrifices                      ,(21,0))
        infoSizer.Add(Chants                          ,(22,0))
        infoSizer.Add(Incantations                    ,(23,0))
        infoSizer.Add(Song                            ,(24,0))
        infoSizer.Add(Dance                           ,(25,0))
        infoSizer.Add(Ritual                          ,(26,0))
        infoSizer.Add(Celebration                     ,(27,0))
        infoSizer.Add(OtherTechniques                 ,(28,0))
        infoSizer.Add(NotesTechniques                 ,(29,0))   

        infoSizer.Add(labelChurch                     ,(0,4))
        infoSizer.Add(Dogmatizer                      ,(1,4))
        infoSizer.Add(EmbustaroLiar                   ,(2,4))
        infoSizer.Add(Hecicero                        ,(3,4))
        infoSizer.Add(Brujo                           ,(4,4))
        infoSizer.Add(Sortilejo                       ,(5,4))
        infoSizer.Add(SacristanHelper                 ,(6,4))
        infoSizer.Add(ChichaMaker                     ,(7,4))
        infoSizer.Add(RelapserBackslider              ,(8,4))
        infoSizer.Add(OtherChurchClass                ,(9,4))

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
        infoSizer.Add(OtherCondition                  ,(13,8))
        
        
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
        infoSizer.Add(OtherPunishment                 ,(11,12))











        

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)

        self.SetSizer(sizer)
        
        
        
        
        
        
        
