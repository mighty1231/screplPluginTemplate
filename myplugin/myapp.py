"""Application template for SC-REPL

When given app is on foreground, a series of methods is executed in each frame as follows.

Case 1. app starts with get_app_manager().start_application(app)
  - on_init, (on_chat), loop, print

Case 2. If 'on_chat' or 'loop' invoked 'get_app_manager().request_update()',
  - (on_chat), loop, print

Case 3. If 'on_chat' or 'loop' did not invoked 'get_app_manager().request_update()',
  - (on_chat), loop

Case 4. If 'on_chat' or 'loop' invoked 'get_app_manager().request_destruct()'
  - (on_chat), loop, on_destruct

Case 5. Previously launched app is dead,
  - on_resume, (on_chat), loop
"""

from eudplib import *

from screpl.core.application import Application
from screpl.core.appcommand import AppCommand
from screpl.core.appmethod import AppTypedMethod
from screpl.encoder.const import ArgEncNumber

# import global variables from __init__.py
from . import app_manager

class MyApp(Application):
    """Custom Application declaration

    Fill attribute 'fields' as fields that your application may use.
    """
    fields = []

    def on_init(self):
        """Called once when the application initialized and goes foreground

        Caution. avoid to use lshift (ex. self.var1 << 0)
        """
        pass

    def on_destruct(self):
        """Called when the application is going to be destructed

        You should free variable that had allocated on on_init()
        """
        pass

    def on_chat(self, address):
        """Called when the super user has chatted something.

        :param address: address of chat from super user.
        :type address: EUDVariable

        It parses it and execute appropriate 'AppCommand' as default behavior
        """
        Application.on_chat(self, address)

    def on_resume(self):
        """Called exactly once after previously started app is destructed
        and the app became to be foreground again"""
        pass

    def loop(self):
        """Called exactly once in every frame

        Define your triggers executed on every frame when the app is on foreground
        """
        if EUDIf()(app_manager.key_press("ESC")):
            app_manager.request_destruct()
            EUDReturn()
        EUDEndIf()
        app_manager.request_update()

    def print(self, writer):
        """Called once in a frame that invoked request_update

        Fill your text UI with given WRITER

        :param writer: writer, whose offset is given to fill display buffer for the app
        :type writer: class:`screpl.utils.byterw.REPLByteRW`

        Check https://mighty1231.github.io/screpl/screpl.utils.byterw.html
        The writer must write null-character after all the contents
        """
        writer.write(0)

    def method_with_no_returns(self, a):
        """Methods without return variables are automatically transformed into AppMethod"""
        pass

    @AppTypedMethod([None, None], [None, None, None])
    def method_with_some_returns(self, a, b):
        """Some methods that should have return must be decorated with AppTypedMethod

        AppTypedMethod(argtypes, rettypes)
        """
        EUDReturn(0, 0, 0)

    @AppCommand([ArgEncNumber, ArgEncNumber])
    def my_command(self, x, y):
        """In-game chat hooks. Chat like "my_command(3, 4)" will execute following triggers"""
        pass
