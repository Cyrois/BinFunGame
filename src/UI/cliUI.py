
import sys
sys.path.insert(0,'/var/www/BinFunGame/src')
#sys.path.insert(0,'C:/Users/Steph/Desktop/Steph/UBC/Y4/T1/Capstone/BinFunGame/src')
import web
from Database import Database
from CSVfile import CSVfile

########################################
#use port 8083
#python cliUI.py 8083
########################################


class cliUI:

    app = None
    render = None
    db = None
    CSVfile = None
    bindata = []
    #location to store files
    relativePath = "/var/www/BinFunGame/src/UI/files/"
    #relativePath = "C:/Users/Steph/Desktop/Steph/UBC/Y4/T1/Capstone/BinFunGame/src/UI/files/"

    def __init__(self):
        urls = ('/', 'cliUI')
        self.render = web.template.render('Website/')
        self.app = web.application(urls, globals())
        #open database
        self.db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")

    @staticmethod
    def startUI():
        BFGclient = cliUI()
        BFGclient.app.run()

    #retrieve data from database, and return csv file to user
    def getData(self, entry):
        print "get Data"
        #clear bindata list before getting new data
        del self.bindata[:]
        self.db.getBinData(self.bindata, entry)
        #create new CSV file to put data in 
        self.CSVfile = CSVfile(self.relativePath, entry['startdate'], entry['enddate'], entry['binlocation'], entry['color'])
        #print returned bin data
        length = len(self.bindata)
        for i in range(0, length):
            ID = self.bindata[i]['ID']
            Location = self.bindata[i]['Location']
            Date = self.bindata[i]['Date']
            Time = self.bindata[i]['Time']
            #put data in CSV file
            target = ID + "," + Location + "," + str(Date) + "," + str(Time)
            self.CSVfile.quickAppend(target)
            print "Entry " + str(i) + ": " + str(ID) + ", " + str(Location) + ", " + str(Date) + ", " + str(Time)

    def GET(self):
        return  self.render.cliUI()
    
    def POST(self):
        print "This is the web input"
        print web.input()
        if(web.input().submit == "False"):
            console.log("do nothing")	
        if(web.input().submit == "True"):
            #user submits entry, return data
            #INPUT FORMAT: 
            #Start Date & End Date: YYYY-MM-DD
            entry = {'startdate':web.input().startdate, 'enddate':web.input().enddate, 'binlocation':web.input().binlocation, 'color':web.input().color}
            self.getData(entry)
        return

if __name__ == '__main__':

    cliUI.startUI()
