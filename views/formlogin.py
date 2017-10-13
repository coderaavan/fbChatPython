from tkinter import StringVar, PhotoImage, Label, Entry, Button, Tk
from views.libs.fbchat1 import *
from fbchat import FBchatUserError
from views.form import Form
from PIL import Image, ImageTk

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

    def _on_buttonlogin_clicked(self):
        username = self.username.get()
        password = self.password.get()
        try:
            client = login(username, password)
            self.close()
            from views.formchatbox import FormChatbox
            chatbox = Tk()
            chatbox.title("fbChat")
            FormChatbox(chatbox, client)
        except FBchatUserError:
            self.close()
            from views.formloginfailure import FormLoginFailure
            err_chatbox = Tk()
            err_chatbox.title("Login Error")
            FormLoginFailure(err_chatbox)

