#!/usr/bin/env python

try:
    from tkinter import *
    from views.formlogin import FormLogin
    from tkinter import font
    from splash import Loader
except ImportError:
    from Tkinter import *
    from views.formlogin import FormLogin


class App:

    def __init__(self,parent_win):
        # creates a child window to the parent
        self.master = Toplevel()
        self.master.update()
        self.master.deiconify() # shows the window thats hidden
        self.master.title("fbChat")
        self.master.geometry("250x100")
        self.currentView = FormLogin(self.master)


if __name__ == "__main__":
    win = Tk()
    app = Loader(win) # this window gets destroyed
    win_app = App(app)
    win.mainloop() # the loop ends when it's destroyed
