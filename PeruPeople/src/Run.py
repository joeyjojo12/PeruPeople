'''
Created on Apr 26, 2014

@author: Eric
'''

import  wx
from gui import PeruListUI

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = PeruListUI.PeruListCtrlFrame()
    app.MainLoop()
