from Display import Display
import web
import globalVars

if __name__ == '__main__':
    globalVars.init()
    Dis = Display()
    Dis.app.run()
