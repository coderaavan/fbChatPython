

from tkinter import *
from tkinter import font
import time

class Loader():

	def __init__(self,master):
		self.master = master
		self.master.title("Loader Anim")
		self.master.geometry("350x200+600+200")
		self.master.resizable(0,0)
		self.master.config(bg = "#4267B2")
		self.master.overrideredirect(1)
		self.someFont = font.Font(family='Ubuntu', size=25, weight='bold')
		self.empty_canvas = Canvas(self.master,width = 300,height=150,bg = "#4267B2",highlightthickness=0).grid(row = 1,column = 1)
		self.lab1 = Label(self.empty_canvas,bg = "#4267B2",text = "facebook",font = self.someFont,fg = "#fff").grid(row = 1,column=1)
		self.loader_canvas = Canvas(self.master,width = 300,height=20,bg = "#4267B2",highlightthickness=0)
		self.loader_canvas.grid(row = 2,column = 1)
		loader_value = 10
        # import the needed stuff here
        #
        #=============================
		while loader_value < 340:
			self.loader = self.loader_canvas.create_rectangle(10,5,loader_value,2,fill = "#fff",width=0)
			loader_value += 10
			time.sleep(0.1)
			self.master.update()
		time.sleep(1)
		#close destroy the window
		self.master.withdraw()


if __name__ == "__main__":
    app = Tk()
    win = Loader(app)
    app.mainloop()
