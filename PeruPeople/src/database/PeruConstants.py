PERU_DB = 'peru.db'

GENDER_LIST = ['M', 'F']
DEFAULT_GENDER = GENDER_LIST[0]

REGION_LIST = ['Coastal','Andes','Jungle']
DEFAULT_REGION = REGION_LIST[0]

AGE_RANGE_LIST = ['0 - 9',
                  '10 - 19',
                  '20 - 29',
                  '30 - 39',
                  '40 - 49',
                  '50 - 59',
                  '60 - 69',
                  '70 - 79',
                  '80 - 89',
                  '90 - 99',
                  '100+']

AGE_RANGE_DEFAULT = AGE_RANGE_LIST[0] 

NUMBER_OF_PEOPLE = 20
TAB_NUMBER_LIST = [str(x) for x in range(1,NUMBER_OF_PEOPLE + 1)]

REFERENCE = 'Reference'
OFFICIAL = 'Official'
PLAINTIFF = 'Plaintiff'
WITNESS = 'Witness'
PROSECUTOR = 'Prosecutor'
DEFENDANT = 'Defendant'


PERSON_FIELDS = ['PersonId','FirstName','LastName','Title','Location','Region','Gender','Age','AgeRange','Occupation','Religion','Notes']
SOURCE_FIELDS = ['SourceId','Citation','Archive','Stack','Number','DocName','Author','Year','Type','Notes']
MATRIX_FIELDS = ['MatrixId',]
