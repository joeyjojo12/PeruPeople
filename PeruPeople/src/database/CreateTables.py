#! /usr/bin/env python3.3
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
  
    con = lite.connect('peru.db')
    
    cur = con.cursor()
    cur.executescript("""
  
        DROP TABLE IF EXISTS PersonGroup;
        DROP TABLE IF EXISTS Entry;
        DROP TABLE IF EXISTS Person;
        DROP TABLE IF EXISTS Source;
        DROP TABLE IF EXISTS Matrix;
        DROP TABLE IF EXISTS RegionType;
        DROP TABLE IF EXISTS DocumentType;
        DROP TABLE IF EXISTS GenderType;
        DROP TABLE IF EXISTS GenderType;
      
       
        CREATE TABLE RegionType (Region    TEXT PRIMARY KEY NOT NULL,
                                 Seq       INTEGER
        );
        
        INSERT INTO RegionType(Region, Seq) VALUES ('Costal', 1);
        INSERT INTO RegionType(Region, Seq) VALUES ('Andes',  2);
        INSERT INTO RegionType(Region, Seq) VALUES ('Jungle', 3);

        CREATE TABLE DocumentType (Document    TEXT PRIMARY KEY NOT NULL,
                                   Seq         INTEGER
        );
        
        INSERT INTO DocumentType(Document, Seq) VALUES ('Book', 1);
        INSERT INTO DocumentType(Document, Seq) VALUES ('Archival',  2);
        
         
        CREATE TABLE CastaType (Casta    TEXT PRIMARY KEY NOT NULL,
                                Seq      INTEGER
        );
        
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

        CREATE TABLE Person(PersonID    INTEGER PRIMARY KEY,
                            FirstName   TEXT,
                            LastName    TEXT,
                            Location    TEXT,
                            Ayllu       TEXT,
                            Region      REFERENCES RegionType(Region),
                            Gender      REFERENCES GenderType(Gender),
                            Casta       REFERENCES CastaType(Casta),
                            Age         INTEGER,
                            AgeRange    INTEGER,
                            Occupation  TEXT,
                            Religion    TEXT,
                            Profession  TEXT,
                            Notes       TEXT
        );
        
        CREATE TABLE Source(SourceId          INTEGER PRIMARY KEY, 
                            Type              REFERENCES DocumentType (Document),
                            Citation          TEXT, 
                            Archive           TEXT, 
                            Stack             TEXT, 
                            PageNumbers       TEXT,
                            Author            TEXT,
                            DocNameTitle      TEXT,
                            Publisher         TEXT,
                            PubPlace          TEXT,
                            Year              INTEGER,
                            ReferencedByFirst TEXT,
                            ReferencedByLast  TEXT,
                            Notes             TEXT
        );

           
        CREATE TABLE Matrix(MatrixID                              INTEGER PRIMARY KEY,        
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
                            YesTortured                           BOOLEAN,    
                            NoTortured                            BOOLEAN,   
                            UnableToDetermineTorture              BOOLEAN,
                            ProfessionFamilySuccession            BOOLEAN,  
                            ProfessionElected                     BOOLEAN,  
                            ProfessionPersonalElection            BOOLEAN,  
                            ProfessionUnableToDetermineProf       BOOLEAN,
                            ConditionBlind                        BOOLEAN,   
                            ConditionOneEyed                      BOOLEAN,   
                            ConditionLame                         BOOLEAN,   
                            ConditionDeaf                         BOOLEAN,   
                            ConditionMute                         BOOLEAN,   
                            ConditionCrippled                     BOOLEAN,   
                            ConditionOtherConditionText           TEXT,
                            YesDevil                              BOOLEAN,   
                            NoDevil                               BOOLEAN,   
                            UnableToDetermineDevil                BOOLEAN,
                            PunishmentWhipped                     BOOLEAN, 
                            PunishmentPublicService               BOOLEAN, 
                            PunishmentCutHair                     BOOLEAN, 
                            PunishmentExecuted                    BOOLEAN, 
                            PunishmentExiled                      BOOLEAN, 
                            PunishmentOtherPunishment             BOOLEAN, 
                            Sacrifices                            BOOLEAN, 
                            Chants                                BOOLEAN, 
                            Incantations                          BOOLEAN, 
                            Song                                  BOOLEAN, 
                            Dance                                 BOOLEAN, 
                            Ritual                                BOOLEAN, 
                            Celebration                           BOOLEAN, 
                            OtherTechniquesText                   TEXT, 
                            NotesTechniquesText                   TEXT, 
                            SpecialClothing                       TEXT, 
                            Cosmology                             TEXT,     
                            Ethnomedicine                         TEXT, 
                            GeneralNotes                          TEXT
        );

        CREATE TABLE Entry(EntryID INTEGER NOT NULL, 
                           PersonGroupID INTEGER,
                           PersonID      INTEGER,
                           SourceID      INTEGER,
                           MatrixID      INTEGER,
                           PRIMARY KEY(EntryID),
                           FOREIGN KEY(PersonGroupID) REFERENCES PersonGroup(PersonGroupID),
                           FOREIGN KEY(PersonID) REFERENCES Person(PersonID)
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
    
  
