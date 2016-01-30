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
scoreboard.dropScoreboardTable()
scoreboard.createScoreboardTable()

test1 = {'name':'Player1','score': 4.324}
test2 = {'name':'MyName','score': 32.5}
test3 = {'name':'Hello','score': 5.98}
test4 = {'name':'Player','score': 1.23}
scoreboard.insertScore(test1)
scoreboard.insertScore(test2)
scoreboard.insertScore(test3)
scoreboard.insertScore(test4)

sblist = []
scoreboard.getTopScores(sblist)
length = len(sblist)
print "TOP 10 SCORES"
for i in range(0, length):
	print sblist[i]
