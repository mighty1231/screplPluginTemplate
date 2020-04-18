'''
Module template for REPL
'''

def onInit():
    from repl import REPL, getAppManager, AppCommand
    from myapp import MyApp

    # MY_COMMAND decides how to invoke the command in-game
    # chatting 'openMyApp()' would create the app
    MY_COMMAND = "openMyApp"
    if "command" in settings:
        MY_COMMAND = settings["command"]

    @AppCommand([])
    def openingCommand(self):
        # At here, 'self' will become REPL instance,
        #    you will not use any functionality of it
        getAppManager().openApplication(MyApp)

    REPL.addCommand(MY_COMMAND, openingCommand)
