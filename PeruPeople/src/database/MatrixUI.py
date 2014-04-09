import wx
import PeruConstants

class MatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        

        label1 = wx.StaticText(self, label="Type of minister :")
        
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
        Curandero                        = self.societal = wx.CheckBox(self, -1, "Curandero/\nCurandera")
        HelperSacristan                  = self.societal = wx.CheckBox(self, -1, "Helper/\nSacristan")
        ChichaAsuacAccacMaker            = self.societal = wx.CheckBox(self, -1, "Chicha/Asuac/\n Accac Maker")
        ChacraLandGuardian               = self.societal = wx.CheckBox(self, -1, "Chacra/\n Land Guardian ")
        BloodsuckersDeathDealersCaptains = self.societal = wx.CheckBox(self, -1, "Bloodsuckers/\n Death Dealers/\n captains")







        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        infoSizer.Add(label1                          ,(1,0))        
        infoSizer.Add(Consulter                       ,(2,1))
        infoSizer.Add(Huaca                           ,(3,2))
        infoSizer.Add(Malqui                          ,(4,2))
        infoSizer.Add(Lightning                       ,(5,2))
        infoSizer.Add(Sun                             ,(6,2))
        infoSizer.Add(Capycocha                       ,(7,2))
        infoSizer.Add(OtherConsulter                  ,(8,2))
        infoSizer.Add(Diviners                        ,(10,1))        
        infoSizer.Add(Spiders                         ,(11,1))
        infoSizer.Add(Molle                           ,(12,1))
        infoSizer.Add(Love                            ,(13,1))
        infoSizer.Add(LostThings                      ,(14,1))
        infoSizer.Add(Mushrooms                       ,(15,1))
        infoSizer.Add(CuyExaminers                    ,(17,1))        
        infoSizer.Add(Purpose                         ,(18,2))        
        infoSizer.Add(Curer                           ,(20,1))        
        infoSizer.Add(Confessor                       ,(22,1))        
        infoSizer.Add(Curandero                       ,(24,1))        
        infoSizer.Add(HelperSacristan                 ,(26,1))        
        infoSizer.Add(ChichaAsuacAccacMaker           ,(28,1))        
        infoSizer.Add(ChacraLandGuardian              ,(30,1))        
        infoSizer.Add(BloodsuckersDeathDealersCaptains,(32,1))        

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)

        self.SetSizer(sizer)
        
        
        
        
        
        
        
