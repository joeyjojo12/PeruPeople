PERU_DB = '../peru.db'

GENDER_LIST = ['M', 'F']
DEFAULT_GENDER = GENDER_LIST[0]

REGION_LIST = ['Coastal','Andes','Jungle']
DEFAULT_REGION = REGION_LIST[0]

DOCUMENT_LIST = ['Book','Archival']
DEFAULT_DOCUMENT = DOCUMENT_LIST[0]

CASTA_LIST = ['Indigenous','Indigenous/Quetcha','Indigenous/Aymara','Spanish','Mestizo','African','Pardos','Mulattos','Zambos','Slave']
DEFAULT_CASTA = CASTA_LIST[0]

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

PERSONGROUP = 'PersonGroup'
PERSON = 'Person'
SOURCE = 'Source'
MATRIX = 'Matrix'
ENTRY  = 'Entry'

PERSONGROUP_ID = 'PersonGroupID'
PERSON_ID = 'PersonID'
SOURCE_ID = 'SourceID'
MATRIX_ID = 'MatrixID'
ENTRY_ID  = 'EntryID'

ENTRY_FIELDS  = ['EntryId','PersonGroupID','PersonID','SourceID','MatrixID']
PERSON_FIELDS = ['PersonID','FirstName','LastName','Location','Ayllu','Region','Gender','Age','AgeRange','Occupation','Religion','Profession','Notes']
SOURCE_FIELDS = ['SourceId','Type','Citation','Archive','Stack','PageNumbers','Author','DocNameTitle','Publisher','PubPlace','Year','ReferencedByFirst','ReferencedByLast','Notes']
MATRIX_FIELDS = ['MatrixId',
                 'Consulter',
                 'ConsulterHuaca',
                 'ConsulterMalqui',
                 'ConsulterLightning',
                 'ConsulterSun',
                 'ConsulterCapycocha',
                 'ConsulterOtherConsulter',
                 'ConsulterOtherConsulterText',
                 'ConsulterGuardianOf',
                 'ConsulterGuardianOfText',
                 'Diviners',
                 'DivinersSpiders',
                 'DivinersMolle',
                 'DivinersLove',
                 'DivinersLostThings',
                 'DivinersMushrooms',
                 'DivinersCuyExaminers',
                 'DivinersPurposeText',
                 'Curer',
                 'Confessor',
                 'Curandero',
                 'HelperSacristan',
                 'ChichaAsuacAccacMaker',
                 'ChacraLandGuardian',
                 'BloodsuckersDeathDealersCaptains',
                 'ChurchDogmatizer',
                 'ChurchEmbustaroLiar',
                 'ChurchHecicero',
                 'ChurchBrujo',
                 'ChurchSortilejo',
                 'ChurchSacristanHelper',
                 'ChurchChichaMaker',
                 'ChurchRelapserBackslider',
                 'ChurchOtherChurchClassText',
                 'TorturedYesTortured',
                 'TorturedNoTortured',
                 'TorturedUnableToDetermineTorture',
                 'ProfessionFamilySuccession',
                 'ProfessionElected',
                 'ProfessionPersonalElection',
                 'ProfessionUnableToDetermineProf',
                 'ConditionBlind',
                 'ConditionOneEyed',
                 'ConditionLame',
                 'ConditionDeaf',
                 'ConditionMute',
                 'ConditionCrippled',
                 'ConditionOtherCondition',
                 'ConditionOtherConditionText',
                 'DevilYesDevil',
                 'DevilNoDevil',
                 'DevilUnableToDetermineDevil',
                 'PunishmentWhipped',
                 'PunishmentPublicService',
                 'PunishmentCutHair',
                 'PunishmentExecuted',
                 'PunishmentExiled',
                 'PunishmentOtherPunishment',
                 'PunishmentOtherPunishmentText',
                 'TechniquesSacrifices',
                 'TechniquesChants',
                 'TechniquesIncantations',
                 'TechniquesSong',
                 'TechniquesDance',
                 'TechniquesRitual',
                 'TechniquesCelebration',
                 'TechniquesOtherTechniques',
                 'TechniquesOtherTechniquesText',
                 'TechniquesNotesTechniquesText',
                 'SpecialClothing',
                 'Cosmology',
                 'Ethnomedicine',
                 'African',
                 'GeneralNotes']

















