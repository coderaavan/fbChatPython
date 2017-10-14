from tkinter import *
from .libs.fbchat1 import *
from .form import Form
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
        self.master.title("fbChat")
        self.master.geometry("350x300")
        self.master.config(bg='#E9EBEE')
        fbphoto = PhotoImage(file='img/FB-f-Logo_blue_58.gif')
        self.fbImageFrame = Frame(master,width=350,height=30,bg='#4267B2')
        self.fblogo = Label(master, image=fbphoto)
        self.fblogo.image = fbphoto
        self.labelid = Label(master, text="Email",fg="#365899",bg="#E9EBEE")
        self.labelpass = Label(master, text="Password",fg="#365899",bg="#E9EBEE")

        self.entryid = Entry(master, textvariable=self.username)
        self.entrypass = Entry(master, show="*", textvariable=self.password)

        self.buttonlogin = Button(master,
                                  text="Login",
                                  command=self._on_buttonlogin_clicked,bg="#3B5970",fg="#F2FFFF",
                                  cursor="hand2",activebackground="#365899",activeforeground="#F2FFFF")

        self.fbImageFrame.grid(row=0, column=0)
        self.fblogo.grid(row=1, column=0,sticky=W,pady = 10,padx=90)

        self.labelid.grid(row=2, column=0,sticky=W,pady = 5,padx=90)
        self.entryid.grid(row=3, column=0,pady=5,ipady=5)

        self.labelpass.grid(row=4, column=0,sticky=W,pady = 5,padx=90)
        self.entrypass.grid(row=5, column=0,pady=5,ipady=5)
        self.buttonlogin.grid(row=6, column=0, columnspan=2,pady=5)

    def _on_buttonlogin_clicked(self):
        username = self.username.get()
        password = self.password.get()
        try:
            client = login(username, password)
            self.close()
            from formchatbox import FormChatbox
            FormChatbox(Tk(), client)

        except FBchatUserError:
            self.close()
            from .formloginfailure import FormLoginFailure
            FormLoginFailure(Tk())
