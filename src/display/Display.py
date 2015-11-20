# Run app.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

# import Buffer
import web
# from time import strftime
count = 0
blackCount = 0
greenCount = 0
blueCount = 0
greyCount = 0


class Display:


    app = None
    my_form = None
    render = None
    

    
    def __init__(self):
        # says map the root URL address to what happens in the
        # tutorial class
        urls = ('/', 'Display')
        # if using templates, tell web.py where to find our
        # HTML templates with render
        self.render = web.template.render('templates/')
        self.app = web.application(urls, globals())
        # creates an HTML text entry box that we render
        self.my_form = web.form.Form(
                                web.form.Textbox('', class_='textfield', id='textfield'),
                                     )
            
    # echo function
    def make_text(self, string):
        global count
        if string == "reset": #change to reset when time is 00:00 (midnight)
            count = 0
            return str(count)
            #zeroString = "Count: " + str(count) + " - Message: '" + string + "' - Time: " + strftime("%Y-%m-%d %H:%M:%S")
            #return zeroString
        elif string != "reset":
            count += 1
            print count
            return str(count)
            #countString = "Count: " + str(count) + " - Message: '" + string + "' - Time: " + strftime("%Y-%m-%d %H:%M:%S")
            #return countString

    def getCount(self,color):
        global blackCount
        global greenCount
        global blueCount
        global greyCount
        if color == "black":
            print "Black Count: " + str(blackCount)
            blackCount += 1
            return blackCount
        elif color == "green":
            print "Green Count: " + str(greenCount)
            greenCount += 1
            return greenCount
        elif color == "blue":
            print "blue Count: " + str(blueCount)
            blueCount += 1
            return blueCount
        elif color == "grey":
            print "grey Count: " + str(greyCount)
            greyCount += 1
            return greyCount
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
        print web.input()
        color =  web.input().color
        print color
        return self.getCount(color)
