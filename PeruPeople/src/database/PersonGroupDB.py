import PeruDB
import PeruConstants

def ListPersonGroups():
    database = PeruDB.PeruDB()
    output = database.querry("SELECT * FROM " + PeruConstants.PERSONGROUP)
    database.closeDB()
    return output

def InsertPersonGroup(database, PersonGroupID):
    output = database.insert("INSERT INTO " + PeruConstants.PERSONGROUP + " VALUES(" + str(PersonGroupID) + ")")
    return output
    
