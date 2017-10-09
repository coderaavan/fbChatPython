#!/usr/bin/env python

import fbchat1 as chat
from Tkinter import *

root = Tk()

username = StringVar()
password = StringVar()

friend = StringVar()
message = StringVar()


def _on_buttonlogin_clicked():
	user = username.get()
	pas = password.get()
	_on_buttonlogin_clicked.client = chat.login(user, pas)
	root.destroy()

def _on_sendbutton_clicked():
	frnd = friendentry.get()
	message = msg.get(1.0, END)
	msg.delete(1.0, END)	
	chat.send_msg(_on_buttonlogin_clicked.client, message, frnd)


labelid = Label(root, text = "LoginID:")
labelpass = Label(root, text ="Password:")

entryid = Entry(root, textvariable = username)
entrypass = Entry(root, show = "*", textvariable = password)

labelid.grid(row = 0, sticky = W)
labelpass.grid(row = 1, sticky = W)

entryid.grid(row = 0, column = 1)
entrypass.grid(row = 1, column = 1)

buttonLogin = Button(root, text = "Login", command = _on_buttonlogin_clicked)
buttonLogin.grid(row = 2, columnspan = 2)

root.mainloop() 


msgbox = Tk()
msg = Text(msgbox, width = 25, height = 5)
msglabel = Label(msgbox, text = "Type your message here:")

friendlabel = Label(msgbox, text = "Name of Friend:")
friendentry = Entry(msgbox, textvariable = friend)

friendlabel.grid(row = 0, sticky = W)
friendentry.grid(row = 0, column = 1, sticky = W)

msglabel.grid(row = 1, sticky = W)
msg.grid(row = 1, column = 1)

sendbutton = Button(msgbox, text = "Send Message", command = _on_sendbutton_clicked)
sendbutton.grid(row = 2, columnspan = 2)

msgbox.mainloop()
