import MySQLdb
import time
import os.path
from Signal import Signal

class Database:
    db = None
    cursor = None
    currentDate = ""
    query = ""
      
    def __init__(self, theHost, theUser, thePsswd, theDB):
        self.db = MySQLdb.connect(theHost, theUser, thePsswd, theDB)
        self.cursor = self.db.cursor()

    #def __init__(self, theHost, thePort, theUser, thePsswd, theDB):
    #    self.db = MySQLdb.connect(host=theHost, port=thePort, user=theUser, passwd=thePsswd, db=theDB)
    #    self.cursor = self.db.cursor()

    def isCurrentDate(self, date):
        return self.currentDate == date
	
    def setCurrentDate(self, date):
        self.currentDate = date

    #generates table name based off of date
    def createBFGTable(self, date):
        print "Creating Table.."
        columns = ["ID","Location","Date","Time"]
        query = "CREATE TABLE " + date + "(" + columns[0] + " VARCHAR(15)," + columns[1] + " VARCHAR(50)," + columns[2] + " DATE NOT NULL," + columns[3] + " TIME" + ");"
        #EX: https://github.com/jat023/CS304_DB/blob/master/src/ca/ubc/cs/cs304/steemproject/access/oraclejdbc/InitializeDatabase.java
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
                print "MySQL Error: " + str(e)
        else:
                print("Table Creation Success")

	#one table per day??
	#table names by date?
    def insertBuffer(self, target):
        print "INSERTING INTO DATABASE"
        date = time.strftime("%d_%m_%Y") #get current date
        if not self.isCurrentDate(date): #check if the date has changed
            self.createBFGTable(date)
            self.setCurrentDate(date)

        for line in target:
            color = Signal.parseSignal(line)[0]
            if not color:
                return;
            location = Signal.parseSignal(line)[1]
            theTime = str(Signal.parseSignal(line)[2])

            #SQL Date format: YYYY-MM-DD
            splitResult = date.split("_")
            theDate = splitResult[2] + "-" + splitResult[1] + "-" + splitResult[0]
            query = "INSERT INTO " + date + " VALUES ( " + "'" + color + "'" + " ," + "'" + location + "'" + " ," + "'" + theDate + "'" + " ," + "'" + theTime + "'" + ");"
            print("Inserting a row: " + query)
            self.cursor.execute(query)
            # Commit your changes in the database
            self.db.commit()
        print "Finished inserting data into the table " + self.currentDate
         
    #database functions for the sorting game application
    #generates table for scores
    def createScoreboardTable(self):
        print "Creating Scoreboard Table.."
        columns = ["Name","Score"]
        query = "CREATE TABLE " + "Scoreboard" + "(" + columns[0] + " VARCHAR(50)," + columns[1] + " INT NOT NULL" + ");"
        #EX: https://github.com/jat023/CS304_DB/blob/master/src/ca/ubc/cs/cs304/steemproject/access/oraclejdbc/InitializeDatabase.java
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
                print "MySQL Error: " + str(e)
        else:
                print("Table Creation Success")

    #insert score into scoreboard for game
    def insertScore(self, target):
        print "INSERTING INTO SCOREBOARD DATABASE"

        for line in target:
            name = Signal.parseSignal(line)[0] #EntryNum
            #make sure entry numbers are different
            score = Signal.parseSignal(line)[1] #Name
            #enter into table
            query = "INSERT INTO " + "Scoreboard" + " VALUES ( " + "'" + name + "'" + " ," + "'" + score + "'" + ");"
            print("Inserting a row: " + query)
            self.cursor.execute(query)
            # Commit your changes in the database
            self.db.commit()
        print "Finished inserting data into the table " + self.currentDate

    #def getTopScores(self):
    #   print "GET TOP 10 SCORES"

    #   query = "SELECT name, score" + "FROM Scoreboard" + "WHERE "
