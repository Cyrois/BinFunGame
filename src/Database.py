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
        date = time.strftime("%d_%m_%Y") #get current date
        if not self.isCurrentDate(date): #check if the date has changed
            self.createBFGTable(date)
            self.setCurrentDate(date)

        for line in target:
            color = Signal.parseSignal(line)[0]
            location = Signal.parseSignal(line)[1]
            theTime = str(Signal.parseSignal(line)[2])

            #SQL Date format: YYYY-MM-DD
            splitResult = date.split("_")
            theDate = splitResult[2] + "-" + splitResult[1] + "-" + splitResult[0]
            if not color:
                return;
            query = "INSERT INTO " + date + " VALUES ( " + "'" + color + "'" + " ," + "'" + location + "'" + " ," + "'" + theDate + "'" + " ," + "'" + theTime + "'" + ");"
            print("Inserting a row: " + query)
            self.cursor.execute(query)
            # Commit your changes in the database
            self.db.commit()
        print "Finished inserting data into the table " + self.currentDate
			
