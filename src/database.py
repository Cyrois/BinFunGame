#!/usr/bin/python
import MySQLdb
#import mysql.connector
#from mysql.connector import errorcode

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="testuser", # your username
                      passwd="password", # your password
                      db="testdb") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()



# Use all the SQL you like
query = "CREATE TABLE Persons( PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar(255), City varchar(255));"
try: cur.execute(query)
except MySQLdb.Error, e:
        print "MySQL Error: " + str(e)
else:
        print("Table Creation Success")
        
query = "INSERT INTO Persons VALUES (50, 'TestLN', 'TestFN', 'TestStreet', 'TestCity');"
cur.execute(query)
query = "INSERT INTO Persons VALUES (51, 'TestLN2', 'TestFN2', 'TestStreet2', 'TestCity2');"
cur.execute(query)

cur.execute("SELECT * FROM Persons")

print "Printing Table.."

# print all the first cell of all the rows
for row in cur.fetchall():
	print row

print "Done"
