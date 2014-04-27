import PeruDB
import PeruConstants

def EntryInsertFromList(entries):
    resultString = ""
    
    for entry in entries:
        result = EntryInsertStatement(entry)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def EntryReadSingleStatement(fields):    
    return("SELECT * FROM ENTRY WHERE " + PeruConstants.ENTRY_FIELDS[0] + " = '" + fields[0] + "';\n")

def EntryInsertStatement(fields):
    
    if len(fields) > len(PeruConstants.ENTRY_FIELDS) or len(fields) < (len(PeruConstants.ENTRY_FIELDS) - 1):
        return -1
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.ENTRY_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.ENTRY + 
                "(" + ",".join(PeruConstants.ENTRY_FIELDS[1:]) + ")" +
                " VALUES(" + "\',\'".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.ENTRY + " (" + ",".join(PeruConstants.ENTRY_FIELDS[1:]) + ")" + " VALUES('" + "','".join(strFields[1:]) + "');\n"

def EntryUpdateStatement(fields):
    
    if len(fields) != len(PeruConstants.ENTRY_FIELDS):
        return -1
    
    strFields = [(PeruConstants.ENTRY_FIELDS[i] + " = '" + str(fields[i]) + "'")  for i in range(1, len(fields))]
    
    return ("UPDATE ENTRY" +
            " SET " + ",".join(strFields) + 
            " WHERE " + PeruConstants.ENTRY_FIELDS[0] + " = " + str(fields[0]) + ";\n")

def EntryDeleteStatement(fields):    
    return("DELETE FROM ENTRY WHERE " + PeruConstants.ENTRY_FIELDS[0] + " = " + fields[0] + ";\n")

def ReadEntry(fields):
    database = PeruDB.PeruDB()
    output = database.querry(EntryReadSingleStatement(fields));
    database.closeDB()
    return output
    
    
def InsertUpdateEntry(database, fields):
    if fields[0] != '':
        return UpdateEntry(database, fields)
    else:
        return InsertEntry(database, fields)
        

def InsertEntry(database, fields):
    output = database.insert(EntryInsertStatement(fields))
    return output

def UpdateEntry(database, fields):
    output = database.update(EntryUpdateStatement(fields))
    return output

def DeleteEntry(database, fields):    
    output = database.delete(EntryDeleteStatement(fields))
    return output

def EntryReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.ENTRY + " WHERE EntryId = " + ID + ";\n"
