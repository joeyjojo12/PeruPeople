import wx
import PeruConstants

class MatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        

        label1 = wx.statictext(self, label="type of minister :")
        
        Consulter = self.societal = wx.checkbox(self, -1, "Consulter")
        Huaca = self.societal = wx.checkbox(self, -1, "Huaca")
        Malqui = self.societal = wx.checkbox(self, -1, "Malqui/Muñaos")
        Lightning = self.societal = wx.checkbox(self, -1, "Lightning")
        Sun = self.Societal = wx.CheckBox(self, -1, "Sun")
        Capycocha = self.Societal = wx.CheckBox(self, -1, "Capycocha")
        OtherConsulter = self.Societal = wx.CheckBox(self, -1, "Other")

        Diviners = self.societal = wx.checkbox(self, -1, "Diviners")
        Spiders = self.societal = wx.checkbox(self, -1, "Spiders (Ex: Pacharicucc or Pachacaricc or Pachacucc)")
        Molle = self.societal = wx.checkbox(self, -1, "Molle (Ex: Rapiac)")
        Love = self.societal = wx.checkbox(self, -1, "Love")
        LostThings = self.Societal = wx.CheckBox(self, -1, "Lost things (Ex. Moscocc)")
        Mushrooms = self.Societal = wx.CheckBox(self, -1, "Mushrooms")
 
        CuyExaminers = self.societal = wx.checkbox(self, -1, "Cuy Examiners (Ex. Hacaricucc o Cuyricucc)")
        Purpose = self.societal = wx.checkbox(self, -1, "Purpose")
        
        Curer = self.societal = wx.checkbox(self, -1, "Curer (Ex: Macsa or Viha)")

        Confessor = self.societal = wx.checkbox(self, -1, "Confessor (Ex: Aucachic/Ychuris in Cuzco)")

        Curandero = self.societal = wx.checkbox(self, -1, "Curandero/Curandera")

        HelperSacristan = self.societal = wx.checkbox(self, -1, "Helper/Sacristan (Ex; Yanapac)")

        ChichaAsuacAccacMaker = self.societal = wx.checkbox(self, -1, "Chicha/Asuac/ Accac Maker")

        ChacraLandGuardian = self.societal = wx.checkbox(self, -1, "Chacra/ Land Guardian (Ex: Ministros de los Parianas)")

        BloodsuckersDeathDealersCaptains = self.societal = wx.checkbox(self, -1, "Bloodsuckers/ Death Dealers/ captains (Ex: Runapmícuc/ Cauchus)")







        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        infoSizer.Add(label1,   (1,0))        
        infoSizer.Add(Consulter,  (1,1))
        infoSizer.Add(Huaca, (2,1))
        infoSizer.Add(Malqui, (3,1))
        infoSizer.Add(Lightning, (1,2))
        infoSizer.Add(Sun,  (2,2))
        infoSizer.Add(Capycocha,     (3,2))
        
           
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)

        self.SetSizer(sizer)
        
        
        
        
        
        
        
