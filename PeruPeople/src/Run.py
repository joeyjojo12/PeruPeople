'''
Created on Apr 26, 2014

@author: Eric
'''

import  os, wx, datetime, shutil
import Parameters
from gui import PeruListUI

#----------------------------------------------------------------------

def DatabaseBackup():
    if not os.path.exists(Parameters.BACKUP_DIR):
        os.mkdir(Parameters.BACKUP_DIR)
        
    backupdir = Parameters.BACKUP_DIR + 'backup_' + str(datetime.date.today()) + '/'
    
    if not os.path.exists(backupdir):
        os.mkdir(backupdir)
        
    curtime = str(datetime.datetime.now())
        
    backup = backupdir + curtime[curtime.index(' ') + 1:curtime.index('.')].replace(':','-')
    
    shutil.copyfile(Parameters.PERU_DB, backup)
    
if __name__ == "__main__":
    DatabaseBackup()
    app = wx.App(False)
    frame = PeruListUI.PeruListCtrlFrame()
    app.MainLoop()
    
    