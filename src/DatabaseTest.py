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
testInput2 = ["green, TEST1, 03:59:25", "black, nest, 03:59:26"]
#print("Inserting: testInput1")
#db.insertBuffer(testInput1)
#print("Inserting: testInput2")
#db.insertBuffer(testInput2)

print("-----------------------------------")
print("TEST1 - Create/Insert Count")
print("-----------------------------------")
db.setCurrentDate("TEST1")
db.createCountTable("TEST1")
db.insertCount(123,124,125,0)
db.createCountTable("TEST1")
db.insertCount(16,15,13,0)
db.insertCount(24,23,22,0)
#Verified up to here works

print("-----------------------------------")
print("TEST2.0 - createCountTable x2")
print("-----------------------------------")
db.createCountTable("TEST1")
db.createCountTable("TEST1")

print("-----------------------------------")
print("TEST2.1 - mimic updateDatabse")
print("-----------------------------------")
date = time.strftime("%d_%m_%Y")
print("DATE (note period at the end): " + date + ".")
db.createCountTable(date)

print("-----------------------------------")
print("TEST2.2 - updateDatabase")
print("-----------------------------------")
db.updateDatabase(testInput1,66,77,88,99)
db.updateDatabase(testInput1,1,2,3,4)

print("-----------------------------------")
print("TEST3 - PullCount")
print("-----------------------------------")
result = db.pullCount()
print("PullCount1: " + str(result[0]) + "," + str(result[1]) + "," + str(result[2]) + "," + str(result[3]) )
try:
	db.insertCount(16,None,13,0)
except:
	print "Insert didnt work"
result = db.pullCount()
print("PullCount2: " + str(result[0]) + "," + str(result[1]) + "," + str(result[2]) + "," + str(result[3]) )