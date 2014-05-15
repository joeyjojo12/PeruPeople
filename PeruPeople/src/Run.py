'''
Created on Apr 26, 2014

@author: Eric
'''

import  wx
import Parameters
from gui import PeruListUI
from database import PeruDB

#----------------------------------------------------------------------

    
if __name__ == "__main__":
    PeruDB.DatabaseBackup()
    app = wx.App(False)
    frame = PeruListUI.PeruListCtrlFrame()
    app.MainLoop()
    
    