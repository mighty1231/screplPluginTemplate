'''
Application template for REPL

When given app is on foreground, a series of methods is executed in each frame as follows.

Case 1. app starts with getAppManager().startApplication(app)
  - init, (onChat), loop, print

Case 2. If 'onChat' or 'loop' invoked 'getAppManager().requestUpdate()',
  - (onChat), loop, print

Case 3. If 'onChat' or 'loop' did not invoked 'getAppManager().requestUpdate()',
  - (onChat), loop

Case 4. If 'onChat' or 'loop' invoked 'getAppManager().requestDestruct()'
  - (onChat), loop, destruct

Case 5. Previously launched app is dead,
  - onResume, (onChat), loop
  - 
'''

from eudplib import *
from repl import (
    Application,
    AppTypedMethod,
    AppCommand,
    argEncNumber
)

# import global variables from module
from . import manager

class MyApp(Application):
    '''
    Fill your fields
    '''
    fields = []

    def onInit(self):
        '''
        Initialize your application

        Caution. Avoid to use lshift (ex. self.var1 << 0)
        '''
        pass

    def onDestruct(self):
        '''
        You should free variable that had allocated on init()
        '''
        pass

    def onChat(self, stringptr):
        '''
        STRINGPTR: A pointer to string of chat from superuser

        It parses it and execute 'AppCommand' given OFFSET as a string pointer as a default
        '''
        Application.onChat(stringptr)

    def onResume(self):
        '''
        It is executed once after each case that previously launched app was dead
        '''
        pass

    def loop(self):
        '''
        Define your triggers executed on every frame when the app is on foreground
        '''
        if EUDIf()(manager.keyPress("ESC")):
            manager.requestDestruct()
            EUDReturn()
        EUDEndIf()

    def print(self, writer):
        '''
        Fill your text UI with given WRITER
        WRITER is EUDByteRW instance defined on
         - https://github.com/mighty1231/screpl/blob/master/repl/core/eudbyterw.py
        '''
        pass

    def method_with_no_returns(self, a):
        pass

    @AppTypedMethod([None, None], [None, None, None])
    def method_with_some_returns(self, a, b):
        '''
        Some methods that should have return must be decorated with AppTypedMethod
          - AppTypedMethod(argtypes, rettypes)
        '''
        EUDReturn(0, 0, 0)

    @AppCommand([argEncNumber, argEncNumber])
    def my_command(self, x, y):
        '''
        In-game chat hooks. Chat like "my_command(3, 4)" will execute following triggers
        '''
        pass
