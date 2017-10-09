from Tkinter import *


class Form(Frame):

    root = None

    def __init__(self, master):
        Frame.__init__(self, master)
        Form.root = master

    def _initialize(self, master):
        pass

    def _initialize_view(self, master):
        pass
