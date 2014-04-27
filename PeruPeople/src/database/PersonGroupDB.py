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
    
def GetPersonName(personGroupID):
    database = PeruDB.PeruDB()
    output = database.querry("SELECT Person.FirstName, Person.LastName " + 
                             "FROM Entry INNER JOIN Person ON Entry.PersonID = Person.PersonID " + 
                             "WHERE Entry.PersonGroupID = " + str(personGroupID) + ";");
    database.closeDB()
    if(output[0] == 0):
        return output[1][0][0] + " " + output[1][0][1]
    else:
        return -1
    