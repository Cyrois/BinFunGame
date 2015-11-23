import MySQLdb

class Database:
    cursor = None
    db = None
      
    def __init__(self, theHost, theUser, thePsswd, theDB):
        self.db = MySQLdb.connect(host=theHost, # your host, usually localhost
                     user=theUser, # your username
                      passwd=thePsswd, # your password
                      db=theDB # name of the data base
        self.cursor = self.db.cursor()

    def createBFGTable(self, tableName):
        columns = ["ID","Location","Date","Time"]
        query = "CREATE TABLE" + tableName+ "(" + columns[0] + "INT," columns[1] + "VARCHAR(255)," + columns[2] + "DATE NOT NULL," + columns[3] + "VARCHAR(255)" +  ");"
        #todo: make primary/foreign keys
        #EX: https://github.com/jat023/CS304_DB/blob/master/src/ca/ubc/cs/cs304/steemproject/access/oraclejdbc/InitializeDatabase.java
        try: cur.execute(query)
        except MySQLdb.Error, e:
                print "MySQL Error: " + str(e)
        else:
                print("Table Creation Success")
