import sys
#sys.path.insert(0,'/var/www/BinFunGame/src')
sys.path.insert(0,'C:/Users/Steph/Desktop/Steph/UBC/Y4/T1/Capstone/BinFunGame/src')
import web
from Database import Database
from CSVfile import CSVfile

########################################
#use port 8083
#python cliUI.py 8083
########################################



bindata = []
filePath = ""
#location to store files
#relativePath = "/var/www/BinFunGame/src/UI/files/"
relativePath = "C:/Users/Steph/Desktop/Steph/UBC/Y4/T1/Capstone/BinFunGame/src/UI/files/"
urls = ('/', 'default',
        '/downloadfile', 'downloadfile')
render = web.template.render('Website/')
app = web.application(urls, globals(), True)
#open database
db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")

#retrieve data from database, and return csv file to user
def getData(entry):
    #clear bindata list before getting new data
    del bindata[:]
    db.getBinData(bindata, entry)
    #create new CSV file to put data in 
    CSV = CSVfile(relativePath, entry['startdate'], entry['enddate'], entry['binlocation'], entry['color'])
    #get # of entries so they can be added to CSV
    length = len(bindata)
    for i in range(0, length):
        #put data in CSV file
        target = bindata[i]['ID'] + "," + bindata[i]['Location'] + "," + str(bindata[i]['Date']) + "," + str(bindata[i]['Time'])
        CSV.quickAppend(target)
    print "Done putting data into CSV"

class default:
    def GET(self):
        return render.cliUI()
        
    def POST(self):
        print "This is the web input"
        print web.input()
        #if(web.input().submit == "False"):
    		#TODO
        if(web.input().submit == "True"):
            #user submits entry, return data
            #INPUT FORMAT: 
            #Start Date & End Date: YYYY-MM-DD
            entry = {'startdate':web.input().startdate, 'enddate':web.input().enddate, 'binlocation':web.input().binlocation, 'color':web.input().color}
            getData(entry)
            #setting filePath to the path of the requested file
            #so it can be sent to user to download
            global filePath
            filePath = entry['startdate'] + "_" + entry['enddate'] + "_" + entry['binlocation'] + "_" + entry['color'] + ".csv"
        return

class downloadfile:
    def GET(self):
        #sends file to user to download
        #opens up a download window
        global filePath
        f = relativePath + filePath
        getFile = file(f, 'rb')
        web.header('Content-Type','text/csv')
        web.header('Content-disposition', 'attachment; filename=' + filePath)
        return getFile.read()


if __name__ == '__main__':

    app.run()

