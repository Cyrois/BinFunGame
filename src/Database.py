import MySQLdb
import time
import os.path
from datetime import timedelta, date
from Signal import Signal

class Database:
    db = None
    cursor = None
    currentDate = ""
    query = ""
    sbquery = ""
      
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
        #print "Creating Count Table.."
        columns = ["Black","Green","Blue","Grey"]
        query = "CREATE TABLE " + date + "_Count" + "(" + columns[0] + " INT," + columns[1] + " INT," + columns[2] + " INT," + columns[3] + " INT" + ");"
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
            pass
            #print "MySQL Error: " + str(e)
        else:
            query = "INSERT INTO " + date + "_Count" + " VALUES ( " + str(0) + "," + str(0) + "," + str(0) + "," + str(0) + ");"
            self.cursor.execute(query)
            
    def insertCount(self, black, green, blue, grey):
        query = "UPDATE " + self.currentDate + "_Count" + " SET Black =" + str(black) + ",Green =" + str(green) + ",Blue =" + str(blue) + ",Grey = " + str(grey) + ";" #WHERE some_column=some_value;
        #print "Inserting Count.."
        #query = "DELETE FROM " + self.currentDate + "_Count" + ";"
        #queryTwo = "INSERT INTO " + self.currentDate + "_Count" + " VALUES ( " + str(black) + "," + str(green) + "," + str(blue) + "," + str(grey) + ");"
        self.cursor.execute(query)
        #self.cursor.execute(queryTwo)
        self.db.commit()
    
    #generates a BFG table with name based off of date
    def createBFGTable(self, date):
        #print "Creating BFG Table.."
        columns = ["ID","Location","Date","Time"]
        query = "CREATE TABLE " + date + "(" + columns[0] + " VARCHAR(15)," + columns[1] + " VARCHAR(50)," + columns[2] + " DATE NOT NULL," + columns[3] + " TIME" + ");"
        #EX: https://github.com/jat023/CS304_DB/blob/master/src/ca/ubc/cs/cs304/steemproject/access/oraclejdbc/InitializeDatabase.java
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
            pass
            #print "MySQL Error: " + str(e)
        else:
            pass
            #print("Table Creation Success")
    
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
            splitResult = self.currentDate.split("_")
            theDate = splitResult[2] + "-" + splitResult[1] + "-" + splitResult[0]
            query = "INSERT INTO " + self.currentDate + " VALUES ( " + "'" + color + "'" + " ," + "'" + location + "'" + " ," + "'" + theDate + "'" + " ," + "'" + theTime + "'" + ");"
            self.cursor.execute(query)
            # Commit your changes in the database
            self.db.commit()
        
    #This is for the server (Html.py)
    #Select: http://zetcode.com/db/mysqlpython/
    #there should be only one row in the table
    def pullCount(self):
        print "pulling count from table: " + self.currentDate + "_Count"
        self.setCurrentDate(time.strftime("%d_%m_%Y")) #might be inefficient
        query = "SELECT SQL_NO_CACHE *" + " FROM " + self.currentDate + "_Count;"
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
            pass
            #print "MySQL Error: " + str(e)
        else:
            #print("Pull Success from: " + self.currentDate + "_Count;" )
            rows = self.cursor.fetchall()
            if len(rows) > 0:
                #result = rows[len(rows)-1]
                #print("Result of index " + str((len(rows)-1)) + " is: " + str(rows[len(rows)-1]))
                result = rows[0]
                return result
            else:
                pass
                #print "ERROR: No rows"

    #used by getBinData for the range of dates between start and end inputs
    def daterange(self, start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def getBinData(self, bindata, entry):
        print "GETTING BIN DATA"
        #separate entry into startdate, enddate, binlocation, color
        startdate = entry['startdate']
        enddate = entry['enddate']
        binlocation = entry['binlocation']
        color = entry['color']
        #convert startdate and enddate to use daterange function
        dsplit = startdate.split("-")
        start_date = date(int(dsplit[0]), int(dsplit[1]), int(dsplit[2]))
        dsplit = enddate.split("-")
        end_date = date(int(dsplit[0]), int(dsplit[1]), int(dsplit[2]))
        #start in bindata list
        stlist = 0
        #query for all entries between startdate and enddate
        #SQL Date format: YYYY-MM-DD
        for single_date in self.daterange(start_date, end_date):
            print single_date
            getdate = single_date.strftime("%d_%m_%Y")
            #returning in ID, Location, Date, Time format
            query = "SELECT * FROM %s " % (getdate,) + "WHERE ID='%s' " % (color,) + "AND Location='%s' " % (binlocation,) + "ORDER BY Date ASC, Time ASC;"
            #add error catch, in case table for specific date doesn't exist
            try: self.cursor.execute(query)
            except MySQLdb.Error, e:
                pass
                #print "MySQL Error: " + str(e)
            else:
                pass
                #get # of entries in table
                result = self.cursor.fetchall()
                length = len(result)
                print "length = " + str(length)
                #return scores in bindata list
                for i in range(0, length):
                    ID, Location, Date, Time = result[i]
                    print Time
                    en = {'ID':ID,'Location':Location,'Date':Date,'Time':Time}
                    bindata.insert(stlist+i, en)
                #change start of bindata list
                stlist = length
        #finished compiling all entries
        print "FINISHED GETTING BIN DATA"
            
    def updateDatabase(self, target, black, green, blue, grey):
        #print "INSERTING INTO DATABASE"
        date = time.strftime("%d_%m_%Y") #get current date
        if not self.isCurrentDate(date): #check if the date has changed
            self.createCountTable(date)
            self.createBFGTable(date)
            self.setCurrentDate(date)
            
        self.insertCount(black, green, blue, grey)
        self.insertBuffer(target)


    #database functions for the sorting game application
    #generates table for scores
    def createScoreboardTable(self):
        print "Creating Scoreboard Table.."
        columns = ["Name","Score"]
        sbquery = "CREATE TABLE " + "Scoreboard" + "(" + columns[0] + " VARCHAR(50)," + columns[1] + " FLOAT NOT NULL" + ");"
        try: self.cursor.execute(sbquery)
        except MySQLdb.Error, e:
            print "MySQL Error: " + str(e)
        else:
            print("Table Creation Success")

    #delete scoreboard table
    def dropScoreboardTable(self):
        print "Deleting Scoreboard Table"
        sbquery = "DROP TABLE Scoreboard"
        try: self.cursor.execute(sbquery)
        except MySQLdb.Error, e:
            print "MySQL Error: " + str(e)
        else:
            print("Table Deletion Success")

    #insert score into scoreboard for game
    def insertScore(self, entry):
        print "INSERTING INTO SCOREBOARD DATABASE"
        #get name and score
        name = entry['name']
        #convert score to float value to be stored
        score = float(str(entry['score']))
        #enter new score into table
        sbquery = "INSERT INTO " + "Scoreboard" + " VALUES ( " + "'" + name + "'" + " ," + "'" + "%f" % (score,) + "'" + ");"
        print("Inserting a row: " + sbquery)
        self.cursor.execute(sbquery)
        # Commit your changes in the database
        self.db.commit()

    #get scores from scoreboard table
    def getTopScores(self, sblist):
        print "GET TOP 10 SCORES"
        #sort score by lowest to highest
        sbquery = "SELECT Name, Score FROM Scoreboard ORDER BY Score ASC, Name ASC LIMIT 10"
        self.cursor.execute(sbquery)
        result = self.cursor.fetchall()
        #get amount of score 
        length = len(result)
        print "Number of scores: " + str(length)
        if (length >= 10):
            length = 10
        else:
            #if list does not have 10 scores yet
            for i in range(length, 10):
                entry = {'name':'Anon','score': 99.99}
                sblist.insert(i, entry)
        #return the scores in sblist
        for i in range(0, length):
            name, score = result[i]
            entry = {'name':name,'score':score}
            #print str(i) + ", Name: " + str(name) + ", Time: " + str(score)
            sblist.insert(i, entry)
        print "Finished getting scores"

    ########################################################################    
    #database functions for the accuracy info  
    ########################################################################    
    
    #one table can fit all the accuracy info (one entry per day)
    def createAccuracyTable(self):
        print "Creating Accuracy Table.."
        columns = ["Food","Recyclables","Paper","Garbage","Date"]
        query = "CREATE TABLE " + "Accuracy" + "(" + columns[0] + " INT," + columns[1] + " INT," + columns[2] + " INT," + columns[3] + " INT," + columns[4] + " DATE NOT NULL," + "PRIMARY KEY (" + columns[4] + ")" + ");"
        #EX: https://github.com/jat023/CS304_DB/blob/master/src/ca/ubc/cs/cs304/steemproject/access/oraclejdbc/InitializeDatabase.java
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
            print "MySQL Error: " + str(e)
        else:
            print("Table Creation Success")
            
    def insertAccuracy(self, entry):
        food = entry['food']
        recyclables = entry['recyclables']
        paper = entry['paper']
        garbage = entry['garbage']
        date = entry['date']
        print date
        queryA = "INSERT INTO Accuracy VALUES(" + str(food) + "," + str(recyclables) + "," + str(paper) + "," + str(garbage) + ",'" + date + "') "
        queryB = "ON DUPLICATE KEY UPDATE Food = VALUES(Food), Recyclables = VALUES(Recyclables), Paper = VALUES(Paper), Garbage = VALUES(Garbage)" + ";"
        query = queryA + queryB
        self.cursor.execute(query)
        self.db.commit()
        print "Finished inserting Accuracy"
        
    def pullAccuracy(self, date):
        query = "SELECT * " + "FROM " + "Accuracy " + "WHERE Date = '" + date + "';"
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
            print "MySQL Error: " + str(e)
        else:
            #print("Pull Success")
            rows = self.cursor.fetchall()
            if len(rows) > 0:
                result = rows[0]
                return result
            else:
                print "No rows found"
        
    def turnOff(self):
        self.db.close()
