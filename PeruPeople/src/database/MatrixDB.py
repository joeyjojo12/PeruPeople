import PeruDB
import PeruConstants, CommonFunctions

def MatrixInsertFromList(matricies):
    resultString = ""
    
    for matrix in matricies:
        result = MatrixInsertStatement(matrix)
        if result == -1:
            return result
        resultString += result
    
    return resultString

def MatrixReadSingleStatement(MatrixID):    
    return("SELECT * FROM MATRIX WHERE " + PeruConstants.MATRIX_ID + " = '" + str(MatrixID) + "';\n")

def MatrixInsertStatement(fields):
    if len(fields) > len(PeruConstants.MATRIX_FIELDS) or len(fields) < (len(PeruConstants.MATRIX_FIELDS) - 1):
        return -1
    
    if len(fields) == (len(PeruConstants.MATRIX_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.MATRIX + 
                "(" + ",".join(PeruConstants.MATRIX_FIELDS[1:]) + ")" +
                " VALUES('" + "\',\'".join(fields) + "');\n")
    else:
        return "INSERT INTO " + PeruConstants.MATRIX + " (" + ",".join(PeruConstants.MATRIX_FIELDS[1:]) + ")" + " VALUES('" + "','".join(fields[1:]) + "');\n"

def MatrixUpdateStatement(fields):
    
    if len(fields) != len(PeruConstants.MATRIX_FIELDS):
        return -1
    
    strFields = [(PeruConstants.MATRIX_FIELDS[i] + " = '" + fields[i] + "'")  for i in range(1, len(fields))]
    
    return ("UPDATE MATRIX" +
            " SET " + ",".join(strFields) + 
            " WHERE " + PeruConstants.MATRIX_FIELDS[0] + " = " + fields[0] + ";\n")

def MatrixDeleteStatement(MatrixID):    
    return("DELETE FROM MATRIX WHERE " + PeruConstants.MATRIX_FIELDS[0] + " = '" + str(MatrixID) + "';\n")

def ReadMatrix(MatrixID):
    database = PeruDB.PeruDB()
    output = database.querry(MatrixReadSingleStatement(MatrixID));
    database.closeDB()
    return output
    
    
def InsertUpdateMatrix(database, fields):
    fields = CommonFunctions.FormatFields(fields)
    if fields[0] != '':
        return UpdateMatrix(database, fields)
    else:
        return InsertMatrix(database, fields)
        

def InsertMatrix(database, fields):
    output = database.insert(MatrixInsertStatement(fields))
    return output

def UpdateMatrix(database, fields):
    output = database.update(MatrixUpdateStatement(fields))
    if output[0] == 0:
        output = [0, fields[0]]
    return output

def DeleteMatrix(database, MatrixID):
    output = database.delete(MatrixDeleteStatement(MatrixID))
    return output
