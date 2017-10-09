from Tkinter import *
from libs.fbchat1 import *
from form import *

class FormChatbox(Form):

    def __init__(self, master, client):
        Form.__init__(self, master)
        self._initialize(master, client)
        self._initialize_view(master)

    def _initialize(self, master, client):
        self.client = client
        self.targetFriend = StringVar()

    def _initialize_view(self, master):
        self.labelmessage = Label(master, text = "Type your message here:")
        self.textmessage = Text(master, width = 25, height = 5)

        self.friendlabel = Label(master, text = "Name of friend:")
        self.friendentry = Entry(master, textvariable = self.targetFriend)

        self.sendbutton = Button(master,
                text = "Send Message",
                command = self._on_sendbutton_clicked)

        self.labelmessage.grid(row = 1, sticky = W)
        self.textmessage.grid(row = 1, column = 1)
        self.friendlabel.grid(row = 0, sticky = W)
        self.friendentry.grid(row = 0, column = 1, sticky = W)
        self.sendbutton.grid(row = 2, columnspan = 2)

    def _on_sendbutton_clicked(self):
	frnd = self.friendentry.get()
	self.friendentry.delete(0, END)
	message = self.textmessage.get(1.0, END)
	self.textmessage.delete(1.0, END)	
	send_msg(self.client, message, frnd)
