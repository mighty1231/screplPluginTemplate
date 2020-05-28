"""Plugin template for SC-REPL"""

from eudplib import *
from screpl.apps.repl import REPL
from screpl.core.appcommand import AppCommand
from screpl.main import get_app_manager

# chatting 'start' will start your application
command = "start"

# initialize your global variables at here
app_manager = get_app_manager()

def plugin_setup():
    """Special function that should be defined on SC-REPL plugins

    Initialization of plugin is recommended to be located here.
    Calling trigger is not allowed outside of plugin_setup().
    """
    from .myapp import MyApp

    @AppCommand([])
    def start_command(self):
        """Starting command that be injected to REPL application

        At here, 'self' will become 'REPL' ApplicationInstance
        Note that codes after start_application is not going to be executed
        """
        app_manager.start_application(MyApp)

    REPL.add_command(command, start_command)
