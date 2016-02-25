#!/usr/bin/python
import MySQLdb
import time
import os.path
from Signal import Signal
from Database import Database
#import mysql.connector
#from mysql.connector import errorcode




#db = MySQLdb.connect(host="localhost", # your host, usually localhost
#                     user="bfg", # your username
#                      passwd="bfg123", # your password
#                      db="bfg") # name of the data base

db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")

testInput1 = ["green,TEST1,05:26:25"]
testInput2 = ["black,nest,03:59:26"]
testInput3 = ["black,nest,05:12:01"]
testInput4 = ["black,nest,11:33:56"]
testInput5 = ["black,nest,01:09:22"]
testInput6 = ["black,nest,04:44:34"]
#print("Inserting: testInput1")
#db.insertBuffer(testInput1)
#print("Inserting: testInput2")
#db.insertBuffer(testInput2)

db.updateDatabase(testInput2,1,1,1,1)
db.updateDatabase(testInput4,1,1,1,1)
db.updateDatabase(testInput3,1,1,1,1)
db.updateDatabase(testInput5,1,1,1,1)
db.updateDatabase(testInput6,1,1,1,1)
#db.updateDatabase(testInput1,2,2,2,2)
