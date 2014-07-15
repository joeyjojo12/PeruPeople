import PeruDB, PersonDB, SourceEntryDB, MatrixDB
import PeruConstants

def EntryInsertFromList(entries):
    resultString = ""
    
    for entry in entries:
        result = EntryInsertStatement(entry)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def EntryReadSingleStatement(EntryID):    
    return("SELECT * FROM ENTRY WHERE " + PeruConstants.ENTRY_FIELDS[0] + " = '" + str(EntryID) + "';\n")

def EntryReadAllStatement(PersonGroupID):
    if(int(PersonGroupID) > 0):
        return("SELECT * FROM ENTRY WHERE PersonGroupID = " + str(PersonGroupID) + " ORDER BY EntryID")
    else:
        return("SELECT * FROM ENTRY ORDER BY EntryID")

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

def EntryDeleteStatement(EntryID):    
    return("DELETE FROM ENTRY WHERE " + PeruConstants.ENTRY_FIELDS[0] + " = '" + str(EntryID) + "';\n")

def ReadEntry(EntryID):
    database = PeruDB.PeruDB()
    output = database.querry(EntryReadSingleStatement(EntryID));
    database.closeDB()
    return output

def ReadEntries(PersonGroupID):
    database = PeruDB.PeruDB()
    output = database.querry(EntryReadAllStatement(PersonGroupID));
    database.closeDB()
    return output    
    
def InsertUpdateEntry(database, fields):
    if fields[0] != '':
        #return UpdateEntry(database, fields)
        #Entry currently has no reason to be update. Return empty response
        return [0,[]]
    else:
        return InsertEntry(database, fields)
        

def InsertEntry(database, fields):
    output = database.insert(EntryInsertStatement(fields))
    return output

def UpdateEntry(database, fields):
    output = database.update(EntryUpdateStatement(fields))
    return output

def DeleteEntry(database, EntryID):
    entry = ReadEntry(EntryID)
    if entry[0] != 0:
        return entry
    
    output = PersonDB.DeletePerson(database, entry[1][0][PeruConstants.ENTRY_FIELDS.index('PersonID')])
    if output[0] != 0:
        return output
    
    output = SourceEntryDB.DeleteSourceEntry(database, entry[1][0][PeruConstants.ENTRY_FIELDS.index('SourceEntryId')])
    if output[0] != 0:
        return output
    
    output = MatrixDB.DeleteMatrix(database, entry[1][0][PeruConstants.ENTRY_FIELDS.index('MatrixID')])
    if output[0] != 0:
        return output
    
    output = database.delete(EntryDeleteStatement(EntryID))
    return output

def EntryReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.ENTRY + " WHERE EntryId = " + ID + ";\n"
