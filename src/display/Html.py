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