import sys
import  wx
import  wx.lib.mixins.listctrl  as  listmix
import PeruConstants
from database import SourceDB

class SourceListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)


class SourceListCtrlFrame(wx.Frame):
    def __init__(self, parent, SourceType):
        
        self.SourceType = SourceType
        self.parent = parent
        
        wx.Frame.__init__(self, None, wx.ID_ANY,"Sources",size=(1200,800))
        
        tID = wx.NewId()
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.list = SourceListCtrl(self, tID,
                                 style=wx.LC_REPORT 
                                 | wx.BORDER_NONE
                                 | wx.LC_EDIT_LABELS
                                 | wx.LC_SORT_ASCENDING
                                 )
        sizer.Add(self.list, 1, wx.EXPAND)

        self.PopulateList()

        self.SetSizer(sizer)
        self.SetAutoLayout(True)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
        
        self.list.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.list, 1, wx.EXPAND)
        
        self.SetSizer(self.sizer)

        self.Show()


    def PopulateList(self):
        self.list.ClearAll()
        
        # but since we want images on the column header we have to do it the hard way:
        info = wx.ListItem()
        info.m_mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.m_image = -1
        info.m_format = 0
        info.m_text = "Source"
        self.list.InsertColumnInfo(0, info)
        
        sources = SourceDB.ListSourceByType(self.SourceType)[1]
        
        print(sources)
        
        sourceDict = {}
                
        for source in sources:            
            sourceDict[source[0]] = source[1]
            """
            if(self.SourceType == PeruConstants.BOOK):
                sourceDict[source[0]] = source[1]
            elif(self.SourceType == PeruConstants.ARTICLE):
                sourceDict[source[0]] = source[1]
            elif(self.SourceType == PeruConstants.ARCHIVE):
                sourceDict[source[0]] = source[1]"""
        
        for item in sourceDict.iteritems():
            index = self.list.InsertStringItem(0, item[1])
            self.list.SetItemData(index, item[0])

        self.list.SetColumnWidth(0, 100)

        # show how to select an item
        self.list.SetItemState(5, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

        self.currentItem = 0

    def OnItemSelected(self, event):
        self.currentItem = event.m_itemIndex
        event.Skip()
        
    def OnDoubleClick(self, evt):
        evt.Skip()
        
        SourceID = self.list.GetItemData(self.currentItem)
        print(SourceID)
        
        self.parent.ClearFields()
        self.parent.SourceFields = SourceDB.ReadSource(SourceID)[1][0]
        self.parent.PopulateSourceFields()
        self.parent.ArrangeFields(self.SourceType)
        self.parent.SourceID = SourceID
        self.parent.initialSourceID = SourceID
        self.parent.SourceEntryID = ''
        
        self.Close()
        
        