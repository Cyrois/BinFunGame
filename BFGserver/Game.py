# Run Html.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

# import Buffer
import web
import logging
# from time import strftime

class Game:

    app = None
    my_form = None
    render = None

    def __init__(self):
        urls = ('/', 'Game')
        self.render = web.template.render('templates/')
        self.app = web.application(urls, globals())

    
    @staticmethod
    def startGame():
        BFGGame = Game()
        BFGGame.app.run()
    
    
    def getScoreboardList(self):
        return

    def GET(self):
        return  self.render.Game()
    
    def POST(self):
        return self.getScoreboardList()
    

if __name__ == '__main__':

    Game.startGame()
