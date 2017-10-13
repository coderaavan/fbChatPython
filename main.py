#!/usr/bin/env python

from tkinter import *
from views.formlogin import FormLogin


class App:

    def __init__(self):
        self.master = Tk()
        self.master.title("lol")
        self.master.geometry("350x300+600+300")
        self.currentView = FormLogin(self.master)

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
