import PeruConstants, PeruDB

def PersonInsertFromList(people):
    resultString = ""
    
    for person in people:
        result = PersonInsertStatement(person)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def PersonReadSingleStatement(fields):    
    return("SELECT * FROM PERSON WHERE " + PeruConstants.PERSON_FIELDS[0] + " = '" + fields[0] + "';\n")

def PersonInsertStatement(fields):
    
    if len(fields) > len(PeruConstants.PERSON_FIELDS) or len(fields) < (len(PeruConstants.PERSON_FIELDS) - 1):
        return -1
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.PERSON_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.PERSON + 
                "(" + ",".join(PeruConstants.PERSON_FIELDS[1:]) + ")" +
                " VALUES(" + "\',\'".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.PERSON + " (" + ",".join(PeruConstants.PERSON_FIELDS[1:]) + ")" + " VALUES('" + "','".join(strFields[1:]) + "');\n"

def PersonUpdateStatement(fields):
    
    if len(fields) != len(PeruConstants.PERSON_FIELDS):
        return -1
    
    strFields = [(PeruConstants.PERSON_FIELDS[i] + " = '" + str(fields[i]) + "'")  for i in range(1, len(fields))]
    
    return ("UPDATE PERSON" +
            " SET " + ",".join(strFields) + 
            " WHERE " + PeruConstants.PERSON_FIELDS[0] + " = " + fields[0] + ";\n")

def PersonDeleteStatement(fields):    
    return("DELETE FROM PERSON WHERE " + PeruConstants.PERSON_FIELDS[0] + " = " + fields[0] + ";\n")

def ReadPerson(fields):
    database = PeruDB.PeruDB()
    output = database.querry(PersonReadSingleStatement(fields));
    database.closeDB()
    return output
    
    
def InsertUpdatePerson(fields):
    if fields[0] != '':
        return UpdatePerson(fields)
    else:
        return InsertPerson(fields)
        

def InsertPerson(fields):
    database = PeruDB.PeruDB()
    output = database.insert(PersonInsertStatement(fields))
    database.closeDB()
    return output

def UpdatePerson(fields):
    database = PeruDB.PeruDB()
    output = database.update(PersonUpdateStatement(fields))
    database.closeDB()
    return output

def DeletePerson(fields):
    database = PeruDB.PeruDB()    
    output = database.delete(PersonDeleteStatement(fields))
    database.closeDB()
    return output

def PersonReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.PERSON + " WHERE PersonId = " + ID + ";\n"
