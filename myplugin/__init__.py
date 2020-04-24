'''
Plugin template for SC-REPL
'''

from eudplib import *
from repl import REPL, getAppManager, AppCommand

# chatting 'start' will start your application
command = "start"

# initialize your global variables at here
manager = getAppManager()

'''
Commands used in REPL are defined below.
'''

from .myapp import MyApp

@AppCommand([])
def startCommand(self):
    '''
    At here, 'self' will become REPL instance
    Note that codes after startApplication will not executed
    '''
    getAppManager().startApplication(MyApp)

REPL.addCommand(command, startCommand)
