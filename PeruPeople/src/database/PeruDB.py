import sqlite3 as lite
import sys, datetime, shutil, os
import PeruConstants

curDir = str(os.getcwd()) + '\\'

def DatabaseBackup():
    backupdir = curDir + 'backups\\'

    if not os.path.exists(backupdir):
        os.mkdir(backupdir)
        
    backupdir = backupdir + 'backup_' + str(datetime.date.today()) + '\\'    
    if not os.path.exists(backupdir):
        os.mkdir(backupdir)
        
    curtime = str(datetime.datetime.now())        
    backup = backupdir + curtime[curtime.index(' ') + 1:curtime.index('.')].replace(':','-') + ".db"
    print(backup)
    shutil.copyfile(curDir + PeruConstants.PERU_DB, backup)

class PeruDB:
    
    con = None
    
    def __init__(self):
        self.openDB()
    
    def openDB(self):
        try:
            self.con = lite.connect(curDir + PeruConstants.PERU_DB)
            cur = self.con.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()
    
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        
    
    def closeDB(self):        
        if self.con:
            self.con.close()

    def commit(self):
        if self.con:
            self.con.commit()
    
    def rollback(self):
        if self.con:
            self.con.rollback()
    
    def querry(self, querryString):
        try:
            cur = self.con.cursor()
            cur.execute(querryString)
            return [0, cur.fetchall()]
        
        except lite.Error, e:
            return [1, "Error %s:" % e.args[0]]
            
        except:
            return [1, "Unexpected Error!"]

    def executeCommand(self, commandString):
        try:
            cur = self.con.cursor()
            cur.execute(commandString)
            return[0, cur.lastrowid]
        
        except lite.Error, e:
            return [1, "Error %s:" % e.args[0]]

    def insert(self, commandString):
        return self.executeCommand(commandString)            

    def update(self, commandString):
        return self.executeCommand(commandString)

    def delete(self, commandString):
        return self.executeCommand(commandString)
