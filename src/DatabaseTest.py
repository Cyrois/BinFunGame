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

#test scoreboard
scoreboard = Database("54.218.32.132", "bfguser", "bfg123", "bfg")
scoreboard.createScoreboardTable()

test1 = ["Name,999"]
test2 = ["Player1,333"]
scoreboard.insertScore(test1)
scoreboard.insertScore(test2)



db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")

testInput1 = ["green,nest,05:26:25"]
testInput2 = ["green, nest, 03:59:25", "black, nest, 03:59:26"]

print("Inserting: testInput1")
db.insertBuffer(testInput1)
print("Inserting: testInput2")
db.insertBuffer(testInput2)

