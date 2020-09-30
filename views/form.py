import tkinter as tk
# import Tkinter as tk in Python 2.x

class Form(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

    def _initialize(self, master):
        pass

    def _initialize_view(self, master):
        pass

    def close(self):
        self.master.destroy()
