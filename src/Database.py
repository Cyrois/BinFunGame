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

	#generates a COUNT table with name = DATE_Count
	#One table per day would be fastest. Should delete old tables since they arnt really needed
	#(can use COUNT function on existing signla data to get count values)
	def createCountTable(self, date):
		print "Creating Count Table.."
        columns = ["Black","Green","Blue","Grey"]
		query = "CREATE TABLE " + date + "_Count" + "(" + columns[0] + " INT," + columns[1] + " INT," + columns[2] + " INT," + columns[3] + " INT" + ");"
		try: self.cursor.execute(query)
        except MySQLdb.Error, e:
                print "MySQL Error: " + str(e)
        else:
                print("Table Creation Success")
			
	def insertCount(self, black, green, blue, grey):
		query = "UPDATE " + date + "_count" + " SET Black =" + black + ",Green =" green + ",Blue =" + blue + ",Grey = " + grey + ";" #WHERE some_column=some_value;
		self.cursor.execute(query)
		self.db.commit()
	
	#generates a BFG table with name based off of date
    def createBFGTable(self, date):
        print "Creating BFG Table.."
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
            self.cursor.execute(query)
            # Commit your changes in the database
            self.db.commit()
			
	def updateDatabase(self, target, black, green, blue, grey):
		print "INSERTING INTO DATABASE"
        date = time.strftime("%d_%m_%Y") #get current date
        if not self.isCurrentDate(date): #check if the date has changed
			self.createCountTable(date)
            self.createBFGTable(date)
            self.setCurrentDate(date)
			
		self.insertCount(black, green, blue, grey)
		self.insertBuffer(target)
		
	#Select: http://zetcode.com/db/mysqlpython/
	def pullCount(self):
		query = "SELECT *" + " FROM " + self.currentDate + "_count;"
		self.cursor.execute(query)
		if( cursor.rowcount > 0 )
			rows = cursor.fetchall()
			result = rows[0]
			return result
		else
			print "ERROR: No rows"
