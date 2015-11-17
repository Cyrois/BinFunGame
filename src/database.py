#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="testuser", # your username
                      passwd="password", # your password
                      db="testdb") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
query = "INSERT INTO Persons VALUES (50, 'TestLN', 'TestFN', 'TestStreet', 'TestCity')"
cur.execute(query)

cur.execute("SELECT * FROM Persons")

print "Testing"

# print all the first cell of all the rows
for row in cur.fetchall():
	print "Print Row.."
	print row

print "Done"
