from Tkinter import *
from libs.fbchat1 import *
from form import Form

class FormLogin(Form):

    def __init__(self, master):
        Form.__init__(self, master)
        self._initialize(master)
        self._initialize_view(master)

    def _initialize(self, master):
        self.username = StringVar()
        self.password = StringVar()
        self.friend = StringVar()
        self.message = StringVar()

    def _initialize_view(self, master):
        self.labelid = Label(master, text="LoginID:")
        self.labelpass = Label(master, text="Password:")

        self.entryid = Entry(master, textvariable=self.username)
        self.entrypass = Entry(master, show="*", textvariable=self.password)

        self.buttonlogin = Button(master,
                                  text="Login",
                                  command=self._on_buttonlogin_clicked)

        self.labelid.grid(row=0, sticky=W)
        self.labelpass.grid(row=1, sticky=W)
        self.entryid.grid(row=0, column=1)
        self.entrypass.grid(row=1, column=1)
        self.buttonlogin.grid(row=2, columnspan=2)

    def _on_buttonlogin_clicked(self):
        username = self.username.get()
        password = self.password.get()
        client = login(username, password)
        self.close()
        from formchatbox import FormChatbox
        chatbox = Tk()
        chatbox.title("fbChat")
        FormChatbox(chatbox, client)
