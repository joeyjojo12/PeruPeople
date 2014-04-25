from . import PeruDB
from .. import PeruConstants

def ListPersonGroups():
    database = PeruDB.PeruDB()
    output = database.querry("SELECT * FROM " + PeruConstants.PERSONGROUP)
    database.closeDB()
    return output

def InsertPersonGroup(PersonGroupID):
    database = PeruDB.PeruDB()
    output = database.insert("INSERT INTO " + PeruConstants.PERSONGROUP + " VALUES(" + str(PersonGroupID) + ")")
    database.closeDB()
    return output
    
