# Run app.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

# import Buffer
import web
# from time import strftime

count = 0
blackCount = 0 # Buffer.blackCount
greenCount = 0 # Buffer.greenCount
blueCount = 0 # Buffer.blueCount
greyCount = 0 # Buffer.greyCount

# echo function
def make_text(string):
    global count
    if string == "reset": #change to reset when time is 00:00 (midnight)
        count = 0
        return str(count)
        #zeroString = "Count: " + str(count) + " - Message: '" + string + "' - Time: " + strftime("%Y-%m-%d %H:%M:%S")
        #return zeroString
    elif string != "reset":
        count += 1
        return str(count)
        #countString = "Count: " + str(count) + " - Message: '" + string + "' - Time: " + strftime("%Y-%m-%d %H:%M:%S")
        #return countString

# says map the root URL address to what happens in the
# tutorial class
urls = ('/', 'tutorial')
# if using templates, tell web.py where to find our
# HTML templates with render
render = web.template.render('templates/')

app = web.application(urls, globals())

# creates an HTML text entry box that we render
my_form = web.form.Form(
                        web.form.Textbox('', class_='textfield', id='textfield'),
                        )

# define tutorial class, GET and POST methods define
# the behaviour of our web.py app
class tutorial:
    def GET(self):
        # give copy of the form instance
        form = my_form()
        # using same name tutorial in class def, call,
        # and HTML template are important
        return render.tutorial(form, "0")
        
    def POST(self):
        form = my_form()
        form.validates()
        # access the value of our text field box
        s = form.value['textfield']
        # send to our echo function
        return make_text(s)

if __name__ == '__main__':
    app.run()

