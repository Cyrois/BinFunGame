# Run Html.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

import web
import sys
sys.path.insert(0,'/home/chris/BinFunGame/src')
#sys.path.insert(0,'/var/www/BinFunGame/src')
#sys.path.insert(0,'c:/users/steph/desktop/steph/ubc/y4/capstone/binfunAccuracy/src')
from Database import Database

########################################
#use port 8082
#python Accuracy.py 8082
########################################


class Accuracy:

    app = None
    render = None
    accuracyDB = None

    def __init__(self):
        urls = ('/', 'Accuracy')
        self.render = web.template.render('Website/')
        self.app = web.application(urls, globals())
        self.accuracyDB = Database("54.218.32.132", "bfguser", "bfg123", "bfg")

    @staticmethod
    def startAccuracy():
        BFGAccuracy = Accuracy()
        BFGAccuracy.app.run()
		
    def getAccuracy(self):
        print "getAccuracy"
		#get accuracy from database
        #TODO: make get from database function
		#self.scoredb.getTopScores(self.scoreboardList)

    def insertAccuracy(self,entry):
        print "insertAccuracy"
        self.accuracyDB.insertAccuracy(entry)


    def GET(self):
        return  self.render.Accuracy()
    
    def POST(self):
        print "This is the web input"
        print web.input()
        if(web.input().submit == "False"):
            print "todo"
			#TODO: uncomment after implement that function
            #return self.getAccuracy()
        if(web.input().submit == "True"):
			#TODO: make the database table
            entry = {'food':web.input().food, 'recyclables':web.input().recyclables, 'paper':web.input().paper, 'garbage':web.input().garbage, 'date':web.input().date}
            self.insertAccuracy(entry)
        return

if __name__ == '__main__':

    Accuracy.startAccuracy()
