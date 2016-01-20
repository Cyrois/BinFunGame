# Run Html.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

import web

class Game:

    app = None
    render = None
    entry = {'name': 'Anon','score':'9999'}
    scoreboardList = []

    def __init__(self):
        urls = ('/', 'Game')
        self.render = web.template.render('templates/')
        self.app = web.application(urls, globals())

    
    @staticmethod
    def startGame():
        BFGGame = Game()
        BFGGame.app.run()
    
    
    def getTopScoreboardList(self):
        return self.scoreboardList[0:10]

    def submitToScoreboard(self,entry):
        self.scoreboardList.append(entry)
        print self.scoreboardList
        self.scoreboardList.sort()
        print self.scoreboardList

    def GET(self):
        return  self.render.Game()
    
    def POST(self):
        print web.input()
        if(web.input().submit == "False"):
            return self.getTopScoreboardList()
        #Submit
        if(web.input().submit == "True"):
            self.entry['name'] = web.input().name
            self.entry['score'] = web.input().score
            self.submitToScoreboard(self.entry)
        return

if __name__ == '__main__':

    Game.startGame()
