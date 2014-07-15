import PeruDB
import PeruConstants


def SourceInsertFromList(sources):
    resultString = ""

    for source in sources:
        result = SourceInsertStatement(source)
        if result == -1:
            return result
        resultString += result

    return resultString


def SourceReadSingleStatement(SourceID):
    return("SELECT * FROM SOURCE WHERE " + PeruConstants.SOURCE_ID + " = '" + str(SourceID) + "';\n")


def SourceListByTyepStatement(DocumentType):
    if DocumentType == PeruConstants.BOOK:
        return("SELECT BookTitle FROM Source WHERE DocumentType='Book'")
    elif DocumentType == PeruConstants.ARTICLE:
        return("SELECT ArticleTitle FROM Source WHERE DocumentType='Article'")
    else:
        return("SELECT ArchiveName FROM Source WHERE DocumentType='Archive'")


def SourceInsertStatement(fields):
    if len(fields) > len(PeruConstants.SOURCE_FIELDS) or len(fields) < (len(PeruConstants.SOURCE_FIELDS) - 1):
        return -1

    if len(fields) == (len(PeruConstants.SOURCE_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.SOURCE + 
                "(" + ",".join(PeruConstants.SOURCE_FIELDS[1:]) + ")" +
                " VALUES('" + "\',\'".join(fields) + "');\n")
    else:
        return "INSERT INTO " + PeruConstants.SOURCE + " (" + ",".join(PeruConstants.SOURCE_FIELDS[1:]) + ")" + " VALUES('" + "','".join(fields[1:]) + "');\n"


def SourceUpdateStatement(fields):
    if len(fields) != len(PeruConstants.SOURCE_FIELDS):
        return -1

    strFields = [(PeruConstants.SOURCE_FIELDS[i] + " = '" + fields[i] + "'")  for i in range(1, len(fields))]

    return ("UPDATE SOURCE" +
            " SET " + ",".join(strFields) +
            " WHERE " + PeruConstants.SOURCE_FIELDS[0] +
            " = " + fields[0] + ";\n")


def SourceDeleteStatement(fields):    
    return("DELETE FROM SOURCE WHERE " + PeruConstants.SOURCE_FIELDS[0] + " = " + fields[0] + ";\n")


def ReadSource(SourceID):
    database = PeruDB.PeruDB()
    output = database.querry(SourceReadSingleStatement(SourceID));
    database.closeDB()
    return output


def InsertUpdateSource(database, fields):
    if fields[0] != '':
        return UpdateSource(database, fields)
    else:
        return InsertSource(database, fields)


def InsertSource(database, fields):
    output = database.insert(SourceInsertStatement(fields))
    return output


def UpdateSource(database, fields):
    output = database.update(SourceUpdateStatement(fields))
    return output


def DeleteSource(database, fields):
    output = database.delete(SourceDeleteStatement(fields))
    return output


def ListSourceByType(database, documentType):
    database = PeruDB.PeruDB()
    output = database.querry(SourceListByTyepStatement(documentType));
    database.closeDB()
    return output
