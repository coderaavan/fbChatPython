from Tkinter import *
from libs.fbchat1 import *
from form import Form
from PIL import Image, ImageTk

class FormLogin(Form):

    def __init__(self, master):	
        Form.__init__(self, master)
        self._initialize(master)
        self._initialize_view(master)

    def _initialize(self, master):
        master.bind("<Return>", self._on_buttonlogin_clicked)
	self.username = StringVar()
        self.password = StringVar()
        self.friend = StringVar()
        self.message = StringVar()

    def _initialize_view(self, master):
        self.master.title("fbChat")
        self.master.geometry("250x100")
        fbphoto = PhotoImage(file='img/FB-f-Logo_blue_58.gif')
        self.fblogo = Label(master, image=fbphoto)
        self.fblogo.image = fbphoto
	self.labelid = Label(master, text="LoginID:")
        self.labelpass = Label(master, text="Password:")

        self.entryid = Entry(master, textvariable=self.username)
        self.entrypass = Entry(master, show="*", textvariable=self.password)

        self.buttonlogin = Button(master,
                                  text="Login",
                                  command=self._on_buttonlogin_clicked)
        self.fblogo.grid(row=0, column=0, rowspan=2, pady=5)
        self.labelid.grid(row=0, column=1)
        self.labelpass.grid(row=1, column=1)
        self.entryid.grid(row=0, column=2)
        self.entrypass.grid(row=1, column=2)
        self.buttonlogin.grid(row=2, column=1, columnspan=2)

    def _on_buttonlogin_clicked(self, event=None):
        username = self.username.get()
        password = self.password.get()
        try:
 	    client = login(username, password)
            self.close()
            from formchatbox import FormChatbox
            FormChatbox(Tk(), client)

        except FBchatUserError:
            self.close()
            from formloginfailure import FormLoginFailure
            FormLoginFailure(Tk())

