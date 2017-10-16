
try:
    from tkinter import *
    from .form import Form
    #from tkinter import font
except ImportError:
    from Tkinter import *
    from form import Form


class FormLoginFailure(Form):

    def __init__(self, master):
        Form.__init__(self, master)
        self._initialize(master)
        self._initialize_view(master)

    def _initialize(self, master):
        pass

    def _initialize_view(self, master):
        self.master.title("Login Error")
        self.master.geometry("350x200+600+300")
        self.master.config(bg="#E9EBEE")
        self.master.resizable(0,0)

	self.master.bind("<Return>", self._on_loginagainbutton_clicked)
        #self.master.overrideredirect(1)

        # change the font accordingly
        #self.someFont = font.Font(family='Ubuntu', size=10, weight='normal')

        self.topFrame = Frame(self.master,width=350,height=30,bg="#4267B2")
        self.topFrame.grid(row=0,column=0,ipadx=160)

        self.closebutton = Button(self.topFrame,text="X",command=self._on_loginagainbutton_clicked,bd=0,\
                            bg="#4267B2",activebackground="#4267B2",fg="#FFFFFB",highlightthickness=0,\
                            cursor="hand2",activeforeground="#FFFFFB")
        self.closebutton.grid(row=0,column=0,sticky=W,padx=2,pady=3,ipadx=2,ipady=3)

        self.err_text = Label(master, text="Couldn't log you in. Incorrect Email/Password",\
                            bg='#BE4B49', fg='#FFFFFB')
        self.err_text.grid(row=1,column=0,padx=5,pady=10,ipady=10,ipadx=3)
        self.loginagainbutton = Button(master,
                                         text="Try logging in Again",
                                         command=self._on_loginagainbutton_clicked,cursor="hand2",
                                         bg="#3B5998",fg="#FFFFFB",activebackground="#365899",activeforeground="#FFFFFB")
        self.loginagainbutton.grid(row=2,column=0,pady=30,ipady=5,padx=10)

    def _on_loginagainbutton_clicked(self, event=None):
        self.close()
        try:
            from .formlogin import FormLogin
        except ImportError:
            # python2
            from formlogin import FormLogin
        FormLogin(Tk())
