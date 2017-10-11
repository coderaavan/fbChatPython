#!/usr/bin/env python

from Tkinter import *
from views.formlogin import FormLogin


class App:

    def __init__(self):
        self.master = Tk()
        self.master.title("fbChat")
        self.master.geometry("250x80")
        self.currentView = FormLogin(self.master)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
