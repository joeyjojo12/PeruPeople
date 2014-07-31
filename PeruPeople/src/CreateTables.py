#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys, os
import PeruConstants

try:
    con = lite.connect(str(os.getcwd()) + '\\' + PeruConstants.PERU_DB)
    
    cur = con.cursor()
    cur.executescript("""
  
        DROP TABLE IF EXISTS PersonGroup;
        DROP TABLE IF EXISTS Entry;
        DROP TABLE IF EXISTS Person;
        DROP TABLE IF EXISTS Source;
        DROP TABLE IF EXISTS SourceEntry;
        DROP TABLE IF EXISTS Matrix;
        DROP TABLE IF EXISTS RegionType;
        DROP TABLE IF EXISTS DocumentType;
        DROP TABLE IF EXISTS GenderType;
        DROP TABLE IF EXISTS GenderType;
        DROP TABLE IF EXISTS CastaType;
      
       
        CREATE TABLE RegionType (Region    TEXT PRIMARY KEY NOT NULL,
                                 Seq       INTEGER
        );
        
        INSERT INTO RegionType(Region, Seq) VALUES ('Costal', 1);
        INSERT INTO RegionType(Region, Seq) VALUES ('Andes',  2);
        INSERT INTO RegionType(Region, Seq) VALUES ('Jungle', 3);        
         
        CREATE TABLE CastaType (Casta    TEXT PRIMARY KEY NOT NULL,
                                Seq      INTEGER
        );

        CREATE TABLE DocumentType (Document    TEXT PRIMARY KEY NOT NULL,
                                   Seq         INTEGER
        );
        
        INSERT INTO DocumentType(Document, Seq) VALUES ('Book', 1);
        INSERT INTO DocumentType(Document, Seq) VALUES ('Article',  2);
        INSERT INTO DocumentType(Document, Seq) VALUES ('Archive',  3);
        
        INSERT INTO CastaType(Casta, Seq) VALUES ('Indigenous',         1);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Indigenous/Quetcha', 2);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Indigenous/Aymara',  3);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Spanish',            4);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Mestizo',            5);
        INSERT INTO CastaType(Casta, Seq) VALUES ('African',            6);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Pardos',             7);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Mulattos',           8);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Zambos',             9);
        INSERT INTO CastaType(Casta, Seq) VALUES ('Slave',              10);
    
        CREATE TABLE GenderType (Gender    CHAR(1) PRIMARY KEY NOT NULL,
                                 Seq       INTEGER
        );
        
        INSERT INTO GenderType(Gender, Seq) VALUES ('M', 1);
        INSERT INTO GenderType(Gender, Seq) VALUES ('F', 2);

        CREATE TABLE Person(PersonID                  INTEGER PRIMARY KEY,
                            FirstName                 TEXT,
                            LastName                  TEXT,
                            Location                  TEXT,
                            Ayllu                     TEXT,
                            Region                    REFERENCES RegionType(Region),
                            Gender                    REFERENCES GenderType(Gender),
                            Casta                     REFERENCES CastaType(Casta),
                            Age                       INTEGER,
                            AgeRange                  INTEGER,
                            Profession                TEXT,
                            Occupation                TEXT,
                            ReligionCatholic          BOOLEAN,
                            ReligionNative            BOOLEAN,
                            ReligionOther             BOOLEAN,
                            ReligionOtherText         TEXT,
                            Notes                     TEXT,
                            TagForExample             BOOLEAN
        );
        
        CREATE TABLE Source(SourceId              INTEGER PRIMARY KEY, 
                            DocumentType          REFERENCES DocumentType(Document),
                            BookTitle             TEXT,
                            BookAuthor1           TEXT,
                            BookAuthor2           TEXT,
                            BookAuthor3           TEXT,
                            BookAuthor4           TEXT,
                            BookAuthor5           TEXT,
                            BookPublisher         TEXT,
                            BookPubPlace          TEXT,
                            BookYear              INTEGER,
                            ArticleTitle          TEXT,
                            ArticleAuthor1        TEXT,
                            ArticleAuthor2        TEXT,
                            ArticleAuthor3        TEXT,
                            ArticleAuthor4        TEXT,
                            ArticleAuthor5        TEXT,
                            ArticlePublication    TEXT,
                            ArticleYear           INTEGER,
                            ArticleVolume         TEXT,
                            ArticleIssue          TEXT,
                            ArchiveName           TEXT,
                            ArchiveCollection     TEXT,
                            ArchiveYear           INTEGER,
                            ArchiveMonth          INTEGER, 
                            ArchiveDay            INTEGER,
                            ArchiveStack          TEXT, 
                            ArchiveExpedientes    TEXT
        );
        
        CREATE TABLE SourceEntry(SourceEntryId          INTEGER PRIMARY KEY,
                                 DocumentType           REFERENCES DocumentType(Document),
                                 BookPageNumbers        TEXT,
                                 BookNotes              TEXT,
                                 ArticlePageNumbers     TEXT,
                                 ArticleNotes           TEXT,
                                 ArchivePageNumbers     TEXT,
                                 ArchivePhotoReference  TEXT,
                                 ArchiveNotes           TEXT
        );

           
        CREATE TABLE Matrix(MatrixID                              INTEGER PRIMARY KEY,    
                            ReferencedByFirst                     TEXT,
                            ReferencedByLast                      TEXT,    
                            Consulter                             BOOLEAN,
                            ConsulterHuaca                        BOOLEAN, 
                            ConsulterMalqui                       BOOLEAN,
                            ConsulterLightning                    BOOLEAN,
                            ConsulterSun                          BOOLEAN, 
                            ConsulterCapycocha                    BOOLEAN, 
                            ConsulterOtherConsulter               TEXT, 
                            ConsulterOtherConsulterText           TEXT, 
                            ConsulterGuardianOf                   BOOLEAN,
                            ConsulterGuardianOfText               TEXT, 
                            Diviners                              BOOLEAN,   
                            DivinersSpiders                       BOOLEAN,
                            DivinersMolle                         BOOLEAN,
                            DivinersLove                          BOOLEAN,
                            DivinersLostThings                    BOOLEAN,
                            DivinersMushrooms                     BOOLEAN,
                            DivinersCuyExaminers                  BOOLEAN,
                            DivinersPurposeText                   TEXT,
                            Curer                                 BOOLEAN,  
                            Confessor                             BOOLEAN,  
                            Curandero                             BOOLEAN,  
                            HelperSacristan                       BOOLEAN,  
                            ChichaAsuacAccacMaker                 BOOLEAN,  
                            ChacraLandGuardian                    BOOLEAN,  
                            BloodsuckersDeathDealersCaptains      BOOLEAN, 
                            ChurchDogmatizer                      BOOLEAN, 
                            ChurchEmbustaroLiar                   BOOLEAN,  
                            ChurchHecicero                        BOOLEAN,  
                            ChurchBrujo                           BOOLEAN,  
                            ChurchSortilejo                       BOOLEAN,  
                            ChurchSacristanHelper                 BOOLEAN,  
                            ChurchChichaMaker                     BOOLEAN,  
                            ChurchRelapserBackslider              BOOLEAN,  
                            ChurchOtherChurchClassText            TEXT, 
                            TorturedYesTortured                   BOOLEAN,    
                            TorturedNoTortured                    BOOLEAN,   
                            TorturedUnableToDetermineTorture      BOOLEAN,
                            ProfessionFamilySuccession            BOOLEAN,  
                            ProfessionElected                     BOOLEAN,  
                            ProfessionPersonalElection            BOOLEAN,  
                            ProfessionUnableToDetermineProf       BOOLEAN,
                            ConditionBlind                        BOOLEAN,   
                            ConditionOneEyed                      BOOLEAN,   
                            ConditionLame                         BOOLEAN,   
                            ConditionDeaf                         BOOLEAN,
                            ConditionMute                         BOOLEAN,
                            ConditionDisabled                     BOOLEAN,
                            ConditionDisabledText                 TEXT,
                            ConditionOtherCondition               BOOLEAN,   
                            ConditionOtherConditionText           TEXT,
                            DevilYesDevil                         BOOLEAN,   
                            DevilNoDevil                          BOOLEAN,   
                            DevilUnableToDetermineDevil           BOOLEAN,
                            PunishmentWhipped                     BOOLEAN, 
                            PunishmentPublicService               BOOLEAN, 
                            PunishmentCutHair                     BOOLEAN, 
                            PunishmentExecuted                    BOOLEAN, 
                            PunishmentExiled                      BOOLEAN, 
                            PunishmentOtherPunishment             BOOLEAN,
                            PunishmentOtherPunishmentText         TEXT,
                            TechniquesSacrifices                  BOOLEAN, 
                            TechniquesChants                      BOOLEAN, 
                            TechniquesIncantations                BOOLEAN, 
                            TechniquesSong                        BOOLEAN, 
                            TechniquesDance                       BOOLEAN, 
                            TechniquesRitual                      BOOLEAN, 
                            TechniquesCelebration                 BOOLEAN, 
                            TechniquesOtherTechniques             BOOLEAN, 
                            TechniquesOtherTechniquesText         TEXT, 
                            TechniquesNotesTechniquesText         TEXT, 
                            SpecialClothing                       TEXT, 
                            Cosmology                             TEXT,     
                            Ethnomedicine                         TEXT,     
                            African                               TEXT, 
                            GeneralNotes                          TEXT
        );

        CREATE TABLE Entry(EntryID INTEGER NOT NULL, 
                           PersonGroupID   INTEGER,
                           PersonID        INTEGER,
                           SourceID        INTEGER,
                           SourceEntryId   INTEGER,
                           MatrixID        INTEGER,
                           PRIMARY KEY(EntryID),
                           FOREIGN KEY(PersonGroupID) REFERENCES PersonGroup(PersonGroupID),
                           FOREIGN KEY(SourceID) REFERENCES Source(SourceID),
                           FOREIGN KEY(SourceEntryId) REFERENCES SourceEntry(SourceEntryId),
                           FOREIGN KEY(MatrixID) REFERENCES Matrix(MatrixID)
        );
        
        CREATE TABLE PersonGroup(PersonGroupId INTEGER NOT NULL, 
                                 PRIMARY KEY(PersonGroupId)
        );
        
        """)
    
    con.commit()
    
except lite.Error as e:
  
    if con:
        con.rollback()
      
    print("Error %s:" % e.args[0])
    sys.exit(1)

finally:
  
    if con:
        con.close()
    
  
#
#                            ConsulterCapycocha        BOOLEAN, 
#                            ConsulterOtherConsulter   TEXT,