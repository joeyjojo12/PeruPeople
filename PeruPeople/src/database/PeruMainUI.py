import wx

#Import UI elements
import PeruConstants, EntryUI

class PeruMainUIFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    def __init__(self, parent, EntryInfo, PersonGroupID):
        """Constructor"""
        wx.Frame.__init__(self, parent, wx.ID_ANY,"Traditional Healers - Peru",size=(1200,800))
        
        self.CenterOnScreen()
        self.CreateStatusBar()
        self.SetStatusText("I love you!")

        # Prepare the menu bar test
        menuBar = wx.MenuBar()

        menu1 = wx.Menu()
        menu1.Append(101, "&Close", "Close")
        menuBar.Append(menu1, "&File")
        
        menu2 = wx.Menu()
        menu2.Append(201, "&About", "Program Information")
        menuBar.Append(menu2, "&About")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.CloseWindow, id=101)
        self.Bind(wx.EVT_MENU, self.AboutInfo, id=201)
        
        self.notebook = EntryUI.NestedEntryPanel(self, EntryInfo, PersonGroupID)

        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.saveButton = wx.Button(self, -1, "Save")
        self.buttonSizer.Add(self.saveButton, 0, wx.ALIGN_RIGHT)
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonSave, self.saveButton)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.notebook, 1, wx.EXPAND)
        self.sizer.Add(self.buttonSizer, 0, wx.EXPAND)
        
        self.SetSizer(self.sizer)
        self.Layout()

        self.Show()
        
    def OnButtonSave(self, evt):
        dlg = wx.MessageDialog(self, 'Jeremy, are you sure you want to save this case?', 'Save Case?', wx.YES_NO )
        if dlg.ShowModal() == wx.ID_YES:
            
            self.notebook.SaveEntries()
            
        dlg.Destroy()

    def CloseWindow(self, event):
        self.Close()

    def AboutInfo(self, event):
        dlg = wx.MessageDialog(self, 'Work in progress', 'About', wx.OK )
        dlg.ShowModal()
        dlg.Destroy()
