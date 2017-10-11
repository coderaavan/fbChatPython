from Tkinter import *
from libs.fbchat1 import *
from form import Form

class FormChatbox(Form):

    def __init__(self, master, client):
        Form.__init__(self, master)
        self._initialize(master, client)
        self._initialize_view(master)

    def _initialize(self, master, client):
        self.client = client
        self.targetFriend = StringVar()
        self.group = StringVar()

    def _initialize_view(self, master):
        self.labelmessage = Label(master, text = "Type your message here:")
        self.textmessage = Text(master, width = 25, height = 5)

        self.friendlabel = Label(master, text = "Name of friend:")
        self.friendentry = Entry(master, textvariable = self.targetFriend)

        self.sendbutton = Button(master,
                                 text = "Send Message",
                                 command = self._on_sendbutton_clicked)

        self.logoutbutton = Button(master,
                                   text="Logout",
                                   command=self._on_logoutbutton_clicked)

        self.grouplabel = Label(master, text = "Name of Group:")
        self.groupentry = Entry(master, textvariable = self.group)

        self.labelmessage.grid(row = 2, sticky = W)
        self.textmessage.grid(row = 2, column = 1)
        self.friendlabel.grid(row = 0, sticky = W)
        self.friendentry.grid(row = 0, column = 1, sticky = W)
        self.sendbutton.grid(row = 3, columnspan = 2)
        self.logoutbutton.grid(row = 4, columnspan = 2)
        self.grouplabel.grid(row = 1,sticky = W)
        self.groupentry.grid(row = 1, column = 1, sticky = W)

    def _on_sendbutton_clicked(self):
        inputFriend  = self.friendentry.get()
        inputGroup = self.groupentry.get()
        message = self.textmessage.get(1.0, END)
        self.textmessage.delete(1.0, END)

        friendlist  = inputFriend.split(",")
        grouplist = inputGroup.split(",")

        sendmsg(self.client, message, friendlist, grouplist)

    def _on_logoutbutton_clicked(self):
        if self.client:
            isSuccess = self.client.logout()

            if isSuccess:
                print("Already Logout...")
                Form.root.destroy()
                from formlogin import FormLogin
                loginbox = Tk()
                loginbox.title("fbChat")
                loginbox.geometry("250x80")
                FormLogin(loginbox)

