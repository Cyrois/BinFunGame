# Run app.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

# import Buffer
import web
import globalVars
import logging
# from time import strftime


class Display:

    app = None
    my_form = None
    render = None
    localBlackCount = 0
    localGreenCount = 0
    localBlueCount = 0
    localGreyCount = 0

    def __init__(self):
        # says map the root URL address to what happens in the
        # tutorial class
        localBlackCount = globalVars.blackCount
        localGreenCount = globalVars.greenCount
        localBlueCount = globalVars.blueCount
        localGreyCount = globalVars.greyCount
        urls = ('/', 'Display')
        # if using templates, tell web.py where to find our
        # HTML templates with render
        self.render = web.template.render('templates/')
        self.app = web.application(urls, globals())
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
            #print "Black Count: " + str(globalVars.blackCount)
            #globalVars.blackCount += 1
            return globalVars.blackCount
        elif color == "green":
            #print "Green Count: " + str(globalVars.greenCount)
            #globalVars.greenCount += 2
            return globalVars.greenCount
        elif color == "blue":
            #print "blue Count: " + str(globalVars.blueCount)
            #globalVars.blueCount += 3
            return globalVars.blueCount
        elif color == "grey":
            #print "grey Count: " + str(globalVars.greyCount)
            #globalVars.greyCount += 4
            return globalVars.greyCount
        else:
            print "Error: No color passed"
            return
    

    def GET(self):
        # give copy of the form instance
        form = self.my_form()
        # using same name tutorial in class def, call,
        # and HTML template are important
        return self.render.Display(form, "0")
    """
    def POST(self):
        form = self.my_form()
        form.validates()
        # access the value of our text field box
        s = form.value['textfield']
        # send to our echo function
        return self.make_text(s)
    """
    
    def POST(self):
        # access the value of our text field box
        # send to our echo function
        #print web.input()
        logging.debug(web.input())
        color =  web.input().color
        #print color
        logging.debug(color)
        return self.getCount(color)
