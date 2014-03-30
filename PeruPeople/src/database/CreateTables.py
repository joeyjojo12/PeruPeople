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
        DROP TABLE IF EXISTS GenderType;
      
       
        CREATE TABLE RegionType (Region    TEXT PRIMARY KEY NOT NULL,
                                 Seq       INTEGER
        );
        
        INSERT INTO RegionType(Region, Seq) VALUES ('Costal', 1);
        INSERT INTO RegionType(Region, Seq) VALUES ('Andes',  2);
        INSERT INTO RegionType(Region, Seq) VALUES ('Jungle', 3);
    
        CREATE TABLE GenderType (Gender    CHAR(1) PRIMARY KEY NOT NULL,
                                 Seq       INTEGER
        );
        
        INSERT INTO GenderType(Gender, Seq) VALUES ('M', 1);
        INSERT INTO GenderType(Gender, Seq) VALUES ('F', 2);

        CREATE TABLE Person(PersonID    INTEGER PRIMARY KEY, 
                            Type        REFERENCES PersonType(Type),
                            FristName   TEXT, 
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
        
        CREATE TABLE Source(SourceId     INTEGER PRIMARY KEY, 
                            Citation     TEXT, 
                            Archive      TEXT, 
                            Stack        TEXT, 
                            Number       INTEGER,
                            DocName      TEXT,
                            Author       TEXT,
                            Year         INTEGER,
                            Type         TEXT,
                            Notes        TEXT
        );
        
           
        CREATE TABLE Matrix(MatrixID      INTEGER PRIMARY KEY,
                            Divination    BOOLEAN,
                            Healing       BOOLEAN,
                            Herbs         BOOLEAN,
                            Psychology    BOOLEAN,
                            Rituals       BOOLEAN,
                            Sacrifices    BOOLEAN,
                            Libations     BOOLEAN,
                            Witchcraft    BOOLEAN,
                            Other         TEXT,
                            Notes         TEXT,
        );

        CREATE TABLE Entry(EntryID INTEGER NOT NULL, 
                           PersonGroupID INTEGER PRIMARY KEY, 
                           PersonID      INTEGER PRIMARY KEY,  
                           SourceID      INTEGER PRIMARY KEY,  
                           MatrixID      INTEGER PRIMARY KEY,  
                           FOREIGN KEY(PersonGroupID) REFERENCES Person(PersonGroupID)
                           FOREIGN KEY(PersonID) REFERENCES Person(PersonID)
                           FOREIGN KEY(SourceID) REFERENCES Source(SourceID)
                           FOREIGN KEY(MatrixID) REFERENCES Matrix(MatrixID)
                           PRIMARY KEY(EntryID),
        );
        
        CREATE TABLE PersonGroup(PersonGroupId INTEGER NOT NULL, 
                                 PRIMARY KEY(PersonGroupId),
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
    
  
  
  
  
