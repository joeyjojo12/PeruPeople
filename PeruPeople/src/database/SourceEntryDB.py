import PeruDB
import PeruConstants


def SourceEntryInsertFromList(sources):
    resultString = ""

    for source in sources:
        result = SourceEntryInsertStatement(source)
        if result == -1:
            return result
        resultString += result

    return resultString


def SourceEntryReadSingleStatement(SourceEntryID):
    return("SELECT * FROM SOURCEENTRY WHERE " + PeruConstants.SOURCE_ENTRY_ID + " = '" + str(SourceEntryID) + "';\n")


def SourceEntryInsertStatement(fields):
    if len(fields) > len(PeruConstants.SOURCE_ENTRY_FIELDS) or len(fields) < (len(PeruConstants.SOURCE_ENTRY_FIELDS) - 1):
        return -1

    if len(fields) == (len(PeruConstants.SOURCE_ENTRY_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.SOURCE_ENTRY + 
                "(" + ",".join(PeruConstants.SOURCE_ENTRY_FIELDS[1:]) + ")" +
                " VALUES(" + "\',\'".join(fields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.SOURCE_ENTRY + " (" + ",".join(PeruConstants.SOURCE_ENTRY_FIELDS[1:]) + ")" + " VALUES('" + "','".join(fields[1:]) + "');\n"


def SourceEntryUpdateStatement(fields):
    if len(fields) != len(PeruConstants.SOURCE_ENTRY_FIELDS):
        return -1

    strFields = [(PeruConstants.SOURCE_ENTRY_FIELDS[i] + " = '" + fields[i] + "'")  for i in range(1, len(fields))]

    return ("UPDATE SOURCEENTRY" +
            " SET " + ",".join(strFields) +
            " WHERE " + PeruConstants.SOURCE_ENTRY_FIELDS[0] +
            " = " + fields[0] + ";\n")


def SourceEntryDeleteStatement(SourceEntryID):    
    return("DELETE FROM SOURCEENTRY WHERE " + PeruConstants.SOURCE_ENTRY_FIELDS[0] + " = '" + str(SourceEntryID) + "';\n")


def ReadSourceEntry(SourceEntryID):
    database = PeruDB.PeruDB()
    output = database.querry(SourceEntryReadSingleStatement(SourceEntryID));
    database.closeDB()
    return output


def InsertUpdateSourceEntry(database, fields):
    if fields[0] != '':
        return UpdateSourceEntry(database, fields)
    else:
        return InsertSourceEntry(database, fields)


def InsertSourceEntry(database, fields):
    output = database.insert(SourceEntryInsertStatement(fields))
    return output


def UpdateSourceEntry(database, fields):
    output = database.update(SourceEntryUpdateStatement(fields))
    return output


def DeleteSourceEntry(database, SourceEntryID):
    output = database.delete(SourceEntryDeleteStatement(SourceEntryID))
    return output
