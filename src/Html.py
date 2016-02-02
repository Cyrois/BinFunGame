#!/usr/bin/env python

from Display import Display
from Database import Database
import web
import globalVars
import test
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
def test():
    while (1):
        globalVars.greenCount = input ("Enter green Count: ")
        logging.debug(globalVars.greenCount)
        globalVars.greyCount = input ("Enter grey Count: ")
        logging.debug(globalVars.greyCount)
        globalVars.blueCount = input ("Enter blue Count: ")
        logging.debug(globalVars.blueCount)
        globalVars.blackCount = input ("Enter black Count: ")
        logging.debug(globalVars.blackCount)
    return
    
def databaseStuff():
    db = Database("localhost", "bfguser", "bfg123", "bfg")
    while(1):
        result = db.pullCount()
        if( result != None ):
            #order is black, green, blue, grey
            #todo: check if result length is = 4
            globalVars.blackCount = int(result[0])
            globalVars.greenCount = int(result[1])
            globalVars.blueCount = int(result[2])
            globalVars.greyCount = int(result[3])
        else:
            print("nothing in the db")
        time.sleep(2)

if __name__ == '__main__':
    globalVars.init()

    #t1 = threading.Thread(target=test)
    #t1.start()
    t2 = threading.Thread(target=Display.startDisplay)
    t2.start()
    t3 = threading.Thread(target=databaseStuff)
    t3.start()

    #t1.join()
    t2.join()
    t3.join()
