#!/usr/bin/env python

try:
    from tkinter import *
    from views.formlogin import FormLogin
except ImportError:
    from Tkinter import *
    from views.formlogin import FormLogin


class App:

    def __init__(self):
        self.master = Tk()
        self.currentView = FormLogin(self.master)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
