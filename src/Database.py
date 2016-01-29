import MySQLdb
import time
import os.path
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
        print "Creating Count Table.."
        columns = ["Black","Green","Blue","Grey"]
        query = "CREATE TABLE " + date + "_Count" + "(" + columns[0] + " INT," + columns[1] + " INT," + columns[2] + " INT," + columns[3] + " INT" + ");"
        try: self.cursor.execute(query)
        except MySQLdb.Error, e:
                print "MySQL Error: " + str(e)
        else:
                print("Table Creation Success")
            
    def insertCount(self, black, green, blue, grey):
        query = "UPDATE " + date + "_count" + " SET Black =" + black + ",Green =" + green + ",Blue =" + blue + ",Grey = " + grey + ";" #WHERE some_column=some_value;
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
    #there should be only one row in the table
    def pullCount(self):
        query = "SELECT *" + " FROM " + self.currentDate + "_count;"
        self.cursor.execute(query)
        if( self.cursor.rowcount > 0 ):
            rows = self.cursor.fetchall()
            result = rows[0]
            return result
        else:
            print "ERROR: No rows"


    #database functions for the sorting game application
    #generates table for scores
    def createScoreboardTable(self):
        print "Creating Scoreboard Table.."
        columns = ["Name","Score"]
        sbquery = "CREATE TABLE " + "Scoreboard" + "(" + columns[0] + " VARCHAR(50)," + columns[1] + " INT NOT NULL" + ");"
        #EX: https://github.com/jat023/CS304_DB/blob/master/src/ca/ubc/cs/cs304/steemproject/access/oraclejdbc/InitializeDatabase.java
        try: self.cursor.execute(sbquery)
        except MySQLdb.Error, e:
                print "MySQL Error: " + str(e)
        else:
                print("Table Creation Success")

    #insert score into scoreboard for game
    def insertScore(self, target):
        print "INSERTING INTO SCOREBOARD DATABASE"

        for line in target:
            #get name and score
            name = Signal.parseSignal(line)[0] 
            score = Signal.parseSignal(line)[1]
            #get count of how many scores in table
            sbquery = "SELECT count(*), min(Score) FROM Scoreboard"
            self.cursor.execute(sbquery)
            result = self.cursor.fetchone()
            count, Score = result
            print "Count: " + str(count)
            if (10 <= count):
                #if there are 10 or more scores, remove rank 10 
                sbquery = "SELECT max(Score), Name FROM Scoreboard"
                self.cursor.execute(sbquery)
                result = self.cursor.fetchone()
                Score, Name = result
                print "Score: " + str(Score)
                print "Name: " + str(Name)
                sbquery = "DELETE FROM Scoreboard WHERE Score = %s" % (Score,)
                print "Delete Rank 10"
                self.cursor.execute(sbquery)
                #Commit changes to the database
                self.db.commit()
                print "Finished deleting score"
            #enter new score into table
            sbquery = "INSERT INTO " + "Scoreboard" + " VALUES ( " + "'" + name + "'" + " ," + "'" + score + "'" + ");"
            print("Inserting a row: " + sbquery)
            self.cursor.execute(sbquery)
            # Commit your changes in the database
            self.db.commit()

    #get scores from scoreboard table
    def getTopScores(self, sblist):
       print "GET TOP 10 SCORES"
       #sort score by lowest to highest
       sbquery = "SELECT Name, Score FROM Scoreboard ORDER BY Score ASC, Name ASC"
       self.cursor.execute(sbquery)
       result = self.cursor.fetchall()
       #get amount of score 
       length = len(result)
       print "Number of scores: " + str(length)
       for i in range(0, length):
            name, score = result[i]
            #print str(i) + ", Name: " + str(name) + ", Time: " + str(score)
            sblist.append(i)
            sblist[i] = name, score

       print "Finished getting scores"
