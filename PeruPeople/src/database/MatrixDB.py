import PeruDB
import PeruConstants

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
    
    strFields = [str(field) for field in fields]
    
    if len(fields) == (len(PeruConstants.MATRIX_FIELDS) - 1):
        return ("INSERT INTO " + PeruConstants.MATRIX + 
                "(" + ",".join(PeruConstants.MATRIX_FIELDS[1:]) + ")" +
                " VALUES(" + "\',\'".join(strFields) + ");\n")
    else:
        return "INSERT INTO " + PeruConstants.MATRIX + " (" + ",".join(PeruConstants.MATRIX_FIELDS[1:]) + ")" + " VALUES('" + "','".join(strFields[1:]) + "');\n"

def MatrixUpdateStatement(fields):
    
    if len(fields) != len(PeruConstants.MATRIX_FIELDS):
        return -1
    
    strFields = [(PeruConstants.MATRIX_FIELDS[i] + " = '" + str(fields[i]) + "'")  for i in range(1, len(fields))]
    
    return ("UPDATE MATRIX" +
            " SET " + ",".join(strFields) + 
            " WHERE " + PeruConstants.MATRIX_FIELDS[0] + " = " + fields[0] + ";\n")

def MatrixDeleteStatement(fields):    
    return("DELETE FROM MATRIX WHERE " + PeruConstants.MATRIX_FIELDS[0] + " = " + fields[0] + ";\n")

def ReadMatrix(MatrixID):
    database = PeruDB.PeruDB()
    output = database.querry(MatrixReadSingleStatement(MatrixID));
    database.closeDB()
    return output
    
    
def InsertUpdateMatrix(database, fields):
    if fields[0] != '':
        #return UpdateMatrix(database, fields)
        print("update Matrix")
        return [0]
    else:
        return InsertMatrix(database, fields)
        

def InsertMatrix(database, fields):
    output = database.insert(MatrixInsertStatement(fields))
    return output

def UpdateMatrix(database, fields):
    output = database.update(MatrixUpdateStatement(fields))
    return output

def DeleteMatrix(database, fields):
    output = database.delete(MatrixDeleteStatement(fields))
    return output

def MatrixReadStatement(ID):
    
    return "SELECT * FROM " + PeruConstants.MATRIX + " WHERE MatrixId = " + ID + ";\n"
