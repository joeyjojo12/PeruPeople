import PeruDB
import PeruConstants, CommonFunctions


def PersonInsertFromList(people):
    resultString = ""
    
    for person in people:
        result = PersonInsertStatement(person)
        if result == -1:
            return result
        resultString += result
    
    return resultString


def PersonReadSingleStatement(PersonID):    
    return("SELECT * FROM PERSON WHERE " + PeruConstants.PERSON_ID + " = '" + str(PersonID) + "';\n")


def PersonInsertStatement(fields):    
    if len(fields) > len(PeruConstants.PERSON_FIELDS) or len(fields) < (len(PeruConstants.PERSON_FIELDS) - 1):
        return [1,"Improper format"]
    
    if len(fields) == (len(PeruConstants.PERSON_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.PERSON + 
                "(" + ",".join(PeruConstants.PERSON_FIELDS[1:]) + ")" +
                " VALUES('" + "\',\'".join(fields) + "');\n")
    else:
        return "INSERT INTO " + PeruConstants.PERSON + " (" + ",".join(PeruConstants.PERSON_FIELDS[1:]) + ")" + " VALUES('" + "','".join(fields[1:]) + "');\n"


def PersonUpdateStatement(fields):    
    if len(fields) != len(PeruConstants.PERSON_FIELDS):
        return -1
    
    strFields = [(PeruConstants.PERSON_FIELDS[i] + " = '" + fields[i] + "'")  for i in range(1, len(fields))]
    
    return ("UPDATE PERSON" +
            " SET " + ",".join(strFields) + 
            " WHERE " + PeruConstants.PERSON_FIELDS[0] + " = " + fields[0] + ";\n")

def PersonDeleteStatement(PersonID):    
    return("DELETE FROM PERSON WHERE " + PeruConstants.PERSON_FIELDS[0] + " = '" + str(PersonID) + "';\n")

def ReadPerson(PersonID):
    database = PeruDB.PeruDB()
    output = database.querry(PersonReadSingleStatement(PersonID));
    database.closeDB()
    return output
    
    
def InsertUpdatePerson(database, fields):
    fields = CommonFunctions.FormatFields(fields)
    if fields[0] != '':
        return UpdatePerson(database, fields)
    else:
        return InsertPerson(database, fields)
        

def InsertPerson(database, fields):
    output = database.insert(PersonInsertStatement(fields))
    return output

def UpdatePerson(database, fields):
    output = database.update(PersonUpdateStatement(fields))
    if output[0] == 0:
        output = [0, fields[0]]
    return output

def DeletePerson(database, PersonID):
    output = database.delete(PersonDeleteStatement(PersonID))
    return output