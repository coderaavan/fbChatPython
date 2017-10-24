#!/usr/bin/env python

try:
    from tkinter import *
    from views.formlogin import FormLogin
    from views.splash import SplashScreen
    from tkinter import font
except ImportError:
    from Tkinter import *
    from views.formlogin import FormLogin
    from views.splash import SplashScreen


class App:

    def __init__(self):
        self.master = Tk()
        self.currentWindow = FormLogin(self.master)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    SplashScreen()
    app = App()
    app.run()
