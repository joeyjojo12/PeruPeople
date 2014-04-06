import wx
import PeruConstants

class MatrixPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        
        label1 = wx.StaticText(self, label="Healing Classifications :")
        
        Societal = self.Societal = wx.CheckBox(self, -1, "Societal")
        Financial = self.Financial = wx.CheckBox(self, -1, "Financial/Success")
        Emotional = self.Emotional = wx.CheckBox(self, -1, "Emotional/Psychological")
        Spiritual = self.Spiritual = wx.CheckBox(self, -1, "Spiritual")
        Physical = self.Physical = wx.CheckBox(self, -1, "Physical")
        Curse = self.Curse = wx.CheckBox(self, -1, "Curse/Harm/Malintentions")
        
        label2 = wx.StaticText(self, label="Healing Methods :")
               
        Divination = self.Divination = wx.CheckBox(self, -1, "Divination")
        Rituals1 = self.Rituals1 = wx.CheckBox(self, -1, "Rituals (community)")
        Rituals2 = self.Rituals2 = wx.CheckBox(self, -1, "Rituals (per person/small group)")
        Libations = self.Libations = wx.CheckBox(self, -1, "Libations")
        Protection = self.Protection = wx.CheckBox(self, -1, "Protection/Wards")
        Herbs = self.Herbs = wx.CheckBox(self, -1, "Herbs/Ethnomedicine")
        Prayers = self.Prayers = wx.CheckBox(self, -1, "Prayers/Chants/Words/Spells")
        Sacrifices = self.Sacrifices = wx.CheckBox(self, -1, "Sacrifices")
        Blood = self.Blood = wx.CheckBox(self, -1, "Blood Use")
        Surgery = self.Surgery = wx.CheckBox(self, -1, "Surgery")
        Repentance = self.Repentance = wx.CheckBox(self, -1, "Repentance/Redemption")
        Price = self.Price = wx.CheckBox(self, -1, "Price/Cost of Service")
        Clothing = self.Clothing = wx.CheckBox(self, -1, "Special Clothing Required")
        Music = self.Music = wx.CheckBox(self, -1, "Dance/Singing/Music")
        
        
        label3 = wx.StaticText(self, label="Other1 :")
        Other1 = self.Other1 = wx.TextCtrl(self, size=(150,-1))
        label4 = wx.StaticText(self, label="Other2 :")
        Other2 = self.Other2 = wx.TextCtrl(self, size=(150,-1))
        label5 = wx.StaticText(self, label="Other3 :")
        Other3 = self.Other3 = wx.TextCtrl(self, size=(150,-1))

        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        
        infoSizer.Add(label1,   (1,0))        
        infoSizer.Add(Societal,  (1,1))
        infoSizer.Add(Financial, (2,1))
        infoSizer.Add(Emotional, (3,1))
        infoSizer.Add(Spiritual, (1,2))
        infoSizer.Add(Physical,  (2,2))
        infoSizer.Add(Curse,     (3,2))
        
        infoSizer.Add(label2,    (4,0))
        infoSizer.Add(Divination, (5,1))
        infoSizer.Add(Rituals1,   (6,1))
        infoSizer.Add(Rituals2,   (7,1))
        infoSizer.Add(Libations,  (8,1))
        infoSizer.Add(Protection, (9,1))
        infoSizer.Add(Herbs,      (10,1))
        infoSizer.Add(Prayers,    (11,1))
        
        infoSizer.Add(Sacrifices, (5,2))
        infoSizer.Add(Blood,      (6,2))
        infoSizer.Add(Surgery,    (7,2))
        infoSizer.Add(Repentance, (8,2))
        infoSizer.Add(Price,      (9,2))
        infoSizer.Add(Clothing,   (10,2))
        infoSizer.Add(Music,      (11,2))
        
        infoSizer.Add(label3,    (12,1))
        infoSizer.Add(Other1,     (12,2))
        infoSizer.Add(label4,    (13,1))
        infoSizer.Add(Other2,     (13,2))
        infoSizer.Add(label5,    (14,1))
        infoSizer.Add(Other3,     (14,2))
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)

        self.SetSizer(sizer)
        
        
        
        
        
        
        