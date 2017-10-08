from Tkinter import *
import fbchat1
root=Tk()
username=StringVar()
password=StringVar()
friend=StringVar()
message=StringVar()

def onClick():
	user=username.get()
	pas=password.get()
	onClick.client=fbchat1.login(user,pas)
	root.destroy()

def onClick2():
	frnd=friendentry.get()
	friendentry.delete(0,END)
	message=msg.get(1.0,END)
	msg.delete(1.0,END)	
	fbchat1.sendmsg(onClick.client,message,frnd)
		
labelid=Label(root,text="LoginID:")
labelpass=Label(root,text="Password:")
entryid=Entry(root, textvariable=username)
entrypass=Entry(root, show="*", textvariable=password)
labelid.grid(row=0,sticky=W)
labelpass.grid(row=1,sticky=W)
entryid.grid(row=0, column=1)
entrypass.grid(row=1, column=1)
buttonLogin=Button(root,text="Login",command=onClick)
buttonLogin.grid(row=2, columnspan=2)
root.mainloop() 


msgbox=Tk()
msg=Text(msgbox,width=25, height=5)
msglabel=Label(msgbox,text="Type your message here:")
friendlabel=Label(msgbox,text="Name of Friend:")
friendentry=Entry(msgbox,textvariable=friend)
friendlabel.grid(row=0,sticky=W)
friendentry.grid(row=0, column=1, sticky=W)
msglabel.grid(row=1, sticky=W)
msg.grid(row=1,column=1)
sendbutton=Button(msgbox,text="Send Message",command=onClick2)
sendbutton.grid(row=2,columnspan=2)
msgbox.mainloop()
