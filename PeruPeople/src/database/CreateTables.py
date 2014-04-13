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

           
        CREATE TABLE Matrix(MatrixID                INTEGER PRIMARY KEY,
                            Divination              BOOLEAN,
                            RitualsCommunity        BOOLEAN,
                            RitualsPersongroup      BOOLEAN,
                            Libations               BOOLEAN,
                            Protection              BOOLEAN,
                            Herbs                   BOOLEAN,
                            Prayers                 BOOLEAN,
                            Sacrifices              BOOLEAN,
                            BloodUse                BOOLEAN,
                            Surgery                 BOOLEAN,
                            Repentance              BOOLEAN,
                            Price                   BOOLEAN,
                            SpecialClothing         BOOLEAN,
                            DanceMusic              BOOLEAN,
                            Other1                  TEXT,
                            Other2                  TEXT,
                            Other3                  TEXT,
                            Notes                   TEXT
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
    
  
