#!/usr/bin/python
import MySQLdb
import time
import os.path
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

test1 = ["Name,321"]
test2 = ["Player1,333"]
test3 = ["Test,123"]
test4 = ["Test,5123"]
scoreboard.insertScore(test1)
scoreboard.insertScore(test2)
scoreboard.insertScore(test3)
scoreboard.insertScore(test4)

scoreboard.getTopScores(list)


