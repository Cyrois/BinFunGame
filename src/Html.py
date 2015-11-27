from Display import Display
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
    globalVars.greenCount = input ("Enter green Count: ")
    logging.debug(globalVars.greenCount)
    globalVars.greyCount = input ("Enter grey Count: ")
    logging.debug(globalVars.greyCount)
    globalVars.blueCount = input ("Enter blue Count: ")
    logging.debug(globalVars.blueCount)
    globalVars.blackCount = input ("Enter black Count: ")
    logging.debug(globalVars.blackCount)
    return

if __name__ == '__main__':
    globalVars.init()

    t1 = threading.Thread(target=test)
    t1.start()
    t2 = threading.Thread(target=Display.startDisplay)
    t2.start()

    t1.join()
    t2.join()
