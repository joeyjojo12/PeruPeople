import PeruConstants, PeruDB

def SourceInsertFromList(sources):
    resultString = ""
    
    for source in sources:
        result = SourceInsertStatement(source)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def SourceReadSingleStatement(fields):    
    return("SELECT * FROM SOURCE WHERE " + PeruConstants.SOURCE_FIELDS[0] + " = '" + fields[0] + "';\n")

def SourceInsertStatement(fields):
    
    if len(fields) > len(PeruConstants.SOURCE_FIELDS) or len(fields) < (len(PeruConstants.SOURCE_FIELDS) - 1):
        return -1
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.SOURCE_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.SOURCE + 
                "(" + ",".join(PeruConstants.SOURCE_FIELDS[1:]) + ")" +
                " VALUES(" + "\',\'".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.SOURCE + " (" + ",".join(PeruConstants.SOURCE_FIELDS[1:]) + ")" + " VALUES('" + "','".join(strFields[1:]) + "');\n"

def SourceUpdateStatement(fields):
    
    if len(fields) != len(PeruConstants.SOURCE_FIELDS):
        return -1
    
    strFields = [(PeruConstants.SOURCE_FIELDS[i] + " = '" + str(fields[i]) + "'")  for i in range(1, len(fields))]
    
    return ("UPDATE SOURCE" +
            " SET " + ",".join(strFields) + 
            " WHERE " + PeruConstants.SOURCE_FIELDS[0] + " = " + fields[0] + ";\n")

def SourceDeleteStatement(fields):    
    return("DELETE FROM SOURCE WHERE " + PeruConstants.SOURCE_FIELDS[0] + " = " + fields[0] + ";\n")

def ReadSource(fields):
    database = PeruDB.PeruDB()
    output = database.querry(SourceReadSingleStatement(fields));
    database.closeDB()
    return output
    
    
def InsertUpdateSource(database, fields):
    if fields[0] != '':
        return UpdateSource(database, fields)
    else:
        return InsertSource(database, fields)
        

def InsertSource(database, fields):
    database = PeruDB.PeruDB()
    output = database.insert(SourceInsertStatement(fields))
    database.closeDB()
    return output

def UpdateSource(database, fields):
    database = PeruDB.PeruDB()
    output = database.update(SourceUpdateStatement(fields))
    database.closeDB()
    return output

def DeleteSource(database, fields):
    database = PeruDB.PeruDB()    
    output = database.delete(SourceDeleteStatement(fields))
    database.closeDB()
    return output

def SourceReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.SOURCE + " WHERE SourceId = " + ID + ";\n"
