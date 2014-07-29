
# Replaces single quotes with two single quotes to prep for sql.
def FormatFields(fieldList):
    newList = []
    for field in fieldList:
        newList.append(field.replace("'","''"))
    return newList