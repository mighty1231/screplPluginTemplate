'''
Application template for REPL

Each application has lifecycle as follows

Case 1. app starts with getAppManager().openApplication(app)
  - init, chatCallback, loop, print

Case 2. If 'chatCallback' or 'loop' invoked 'getAppManager().requestUpdate()',
  - chatCallback, loop, print

Case 3. If 'chatCallback' or 'loop' did not invoked 'getAppManager().requestUpdate()',
  - chatCallback, loop

Case 4. if 'chatCallback' or 'loop' invoked 'getAppManager().requestDestruct()'
  - chatCallback, loop, destruct
'''

from eudplib import *
from repl import (
    Application,
    AppTypedMethod,
    AppCommand,
    getAppManager,
    argEncNumber
)

manager = getAppManager()

class MyApp(Application):
    fields = [
        'var1',
        'var2'
    ]

    def init(self):
        '''
        Special parameter. cmderr_epd is 
        Caution. Avoid to use lshift (ex. self.var1 << 0)
        '''
        self.cmd_output_epd = manager.allocDb_epd(16 // 4)
        self.var1 = 0
        self.var2 = 341

    def destruct(self):
        '''
        You should free variable that had allocated on init()
        '''
        manager.freeDb_epd(self.cmd_output_epd)

    def chatCallback(self, offset):
        '''
        Reads command and execute AppCommands given OFFSET as a string pointer
        '''
        MyApp.getSuper().chatCallback(offset)

    def loop(self):
        if EUDIf()(manager.keyPress("ESC")):
            manager.requestDestruct()
            EUDReturn()
        EUDEndIf()

        self.var1 += 1
        self.noReturn(self.var1)
        manager.requestUpdate()

    def print(self, writer):
        '''
        writer.write_f()
        '''
        writer.write_f('var1 = %D\n', self.var1)
        writer.write_f('var2 = %D\n', self.var2)
        writer.write_f('cmd result -> %E', self.cmd_output_epd)

    def noReturn(self, a):
        self.var2 = a // 4

    @AppTypedMethod([None, None], [None, None])
    def someReturns(self, a, b):
        '''
        Some methods that should have return must be decorated with AppTypedMethod
          - AppTypedMethod(argtypes, rettypes)
        '''
        EUDReturn(a+b, a-b)

    @AppCommand([argEncNumber, argEncNumber])
    def plus(self, a, b):
        '''
        In-game chat like "plus(3, 4)" executes this
        '''
        c, d = self.someReturns(a, b)
        self.var1 = c
        self.var2 = d
