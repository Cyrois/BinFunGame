# Run Html.py and load "http://localhost:8080/" in a browser
#!/usr/bin/env python

import web
import sys
sys.path.insert(0,'/var/www/BinFunGame/src')
#sys.path.insert(0,'c:/users/steph/desktop/steph/ubc/y4/capstone/binfungame/src')
from Database import Database

class Game:

    app = None
    render = None
    scoreboardList = []
    scoredb = None

    def __init__(self):
        urls = ('/', 'Game')
        self.render = web.template.render('templates/')
        self.app = web.application(urls, globals())
        #create database for scores
        self.scoredb = Database("54.218.32.132", "bfguser", "bfg123", "bfg")
        #self.scoredb.createScoreboardTable()

    @staticmethod
    def startGame():
        BFGGame = Game()
        BFGGame.app.run()

    def getTopScoreboardList(self):
        self.scoredb.getTopScores(self.scoreboardList)
        print "get top 10"
        print self.scoreboardList[0:10]
        return self.scoreboardList[0:10]

    def submitToScoreboard(self,entry):
        #add score to the database
        self.scoredb.insertScore(entry)

        #self.scoreboardList.append(entry)
        #print "This is scoreboardList"
        #print self.scoreboardList
        #self.scoreboardList.sort()
        #print self.scoreboardList

    def GET(self):
        return  self.render.Game()
    
    def POST(self):
        print "This is the web input"
        print web.input()
        if(web.input().submit == "False"):
            return self.getTopScoreboardList()
        #Submit
        if(web.input().submit == "True"):
            entry = {'name':web.input().name,'score':web.input().score}
            self.submitToScoreboard(entry)
        return

if __name__ == '__main__':

    Game.startGame()
