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

db = Database("localhost", "bfg", "bfg123", "bfg")

testInput1 = ["green,nest,05:26:25"]
testInput2 = ["green, nest, 03:59:25", "black, nest, 03:59:26"]

print("Inserting: testInput1")
db.insertBuffer(testInput1)
print("Inserting: testInput2")
db.insertBuffer(testInput2)

