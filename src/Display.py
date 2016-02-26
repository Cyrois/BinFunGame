# Run Html.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

# import Buffer
import web
import globalVars
import logging
import datetime
from Database import Database
# from time import strftime

class Display:

    app = None
    my_form = None
    render = None
	displayDB = None

    def __init__(self):
        urls = ('/', 'Display')
        # if using templates, tell web.py where to find our
        # HTML templates with render
        self.render = web.template.render('templates/')
        self.app = web.application(urls, globals())
		self.displayDB = Database("54.218.32.132", "bfguser", "bfg123", "bfg")
        # creates an HTML text entry box that we render
        self.my_form = web.form.Form(
                                web.form.Textbox('', class_='textfield', id='textfield'),
                                     )
    
    @staticmethod
    def startDisplay():
        Dis = Display()
        Dis.app.run()
    
    
    def getCount(self,color):
        if color == "black":
            return globalVars.blackCount
        elif color == "green":
            return globalVars.greenCount
        elif color == "blue":
            return globalVars.blueCount
        elif color == "grey":
            return globalVars.greyCount
        else:
            print "Error: No color passed"
            return

    def getAllCount(self):
        colorCount = [globalVars.greenCount,globalVars.greyCount,globalVars.blueCount,globalVars.blackCount]
        return colorCount

    def getAllAccuracy(self):
        #colorAccuracy = [globalVars.greenCount,globalVars.greyCount,globalVars.blueCount,globalVars.blackCount]
		yesterday = date.today() - timedelta(1)
		colorAccuracy = self.displayDB.pullAccuracy(yesterday.strftime("%Y-%d-%m"))
        print colorAccuracy[0]
        return colorAccuracy[0]


    def GET(self):
        # give copy of the form instance
        form = self.my_form()
        # using same name tutorial in class def, call,
        # and HTML template are important
        return self.render.Display(form, "0")
    
    def POST(self):
        if (web.input().type == "accuracy"):
            return self.getAllAccuracy()
        else:
        #logging.debug(web.input())
        #print color
        #logging.debug(self.getAllCount())
            return self.getAllCount()
    
    """
    def POST(self):
        #print web.input()
        logging.debug(web.input())
        color =  web.input().color
        #print color
        logging.debug(color)
        logging.debug(self.getAllCount())
        return self.getCount(color)
    """
