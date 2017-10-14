from Tkinter import *


class Form(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master

    def _initialize(self, master):
        pass

    def _initialize_view(self, master):
        pass

    def close(self):
        self.master.destroy()
