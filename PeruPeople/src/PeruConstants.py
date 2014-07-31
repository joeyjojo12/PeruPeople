import itertools

PERU_DB = 'peru.db'

GENDER_LIST = ['M', 'F']
DEFAULT_GENDER = GENDER_LIST[0]

REGION_LIST = ['Coastal','Andes','Jungle']
DEFAULT_REGION = REGION_LIST[0]

DOCUMENT_LIST = ['Book','Article','Archive']
DEFAULT_DOCUMENT = DOCUMENT_LIST[2]

BOOK = 0
ARTICLE = 1
ARCHIVE = 2

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
SOURCE_ENTRY = 'SourceEntry'
MATRIX = 'Matrix'
ENTRY  = 'Entry'

PERSONGROUP_ID = 'PersonGroupID'
PERSON_ID = 'PersonID'
SOURCE_ID = 'SourceID'
SOURCE_ENTRY_ID = 'SourceEntryID'
MATRIX_ID = 'MatrixID'
ENTRY_ID  = 'EntryID'

ENTRY_FIELDS  = ['EntryID','PersonGroupID','PersonID','SourceID','SourceEntryId','MatrixID']
PERSON_FIELDS = ['PersonID','FirstName','LastName','Location','Ayllu','Region','Gender','Casta','Age','AgeRange','Profession','Occupation','ReligionCatholic','ReligionNative','ReligionOther','ReligionOtherText','Notes','TagForExample']

BOOK_FIELDS = ['BookTitle','BookAuthor1','BookAuthor2','BookAuthor3','BookAuthor4','BookAuthor5','BookPublisher','BookPubPlace','BookYear']
ARTICLE_FIELDS = ['ArticleTitle','ArticleAuthor1','ArticleAuthor2','ArticleAuthor3','ArticleAuthor4','ArticleAuthor5','ArticlePublication','ArticleYear','ArticleVolume','ArticleIssue']
ARCHIVE_FIELDS = ['ArchiveName','ArchiveCollection','ArchiveYear','ArchiveMonth','ArchiveDay','ArchiveStack','ArchiveExpedientes']
SOURCE_FIELDS = list(['SourceId','DocumentType'] + BOOK_FIELDS + ARTICLE_FIELDS + ARCHIVE_FIELDS)

BOOK_ENTRY_FIELDS = ['BookPageNumbers','BookNotes']
ARTICLE_ENTRY_FIELDS = ['ArticlePageNumbers','ArticleNotes']
ARCHIVE_ENTRY_FIELDS = ['ArchivePageNumbers','ArchivePhotoReference','ArchiveNotes']
SOURCE_ENTRY_FIELDS = list(['SourceEntryId','DocumentType'] + BOOK_ENTRY_FIELDS + ARTICLE_ENTRY_FIELDS + ARCHIVE_ENTRY_FIELDS)

MATRIX_FIELDS = ['MatrixID',
                 'ReferencedByFirst',
                 'ReferencedByLast',
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
                 'ConditionDisabled',
                 'ConditionDisabledText',
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



ERROR_SAVING_HEADER = "ERROR SAVING!"
ERROR_SAVING_MESSAGE = "There was an error saving. Let me know about it."

SUCCESSFULL_SAVING_HEADER = "Saved"
SUCCESSFULL_SAVING_MESSAGE = "Successfully saved." 














