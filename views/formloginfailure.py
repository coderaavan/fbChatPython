from tkinter import Text, INSERT, Button, Tk
from views.form import Form


class FormLoginFailure(Form):

    def __init__(self, master):
        Form.__init__(self, master)
        self._initialize(master)
        self._initialize_view(master)

    def _initialize(self, master):
        pass

    def _initialize_view(self, master):
        self.err_text_widget = Text(master, bg='#3b5998', fg='#ffffff', height=5, width=40, font=("TkDefaultFont", "12"))
        self.err_text_widget.insert(INSERT, "Invalid loginID/Password combination!\nPlease try again!")
        self.err_text_widget.pack()
    
        self.loginagainbutton = Button(master,
                                         text="Login Again",
                                         command=self._on_loginagainbutton_clicked)
        self.loginagainbutton.pack()
    def _on_loginagainbutton_clicked(self):
        self.close()
        from views.formlogin import FormLogin
        loginbox = Tk()
        loginbox.title("fbChat")
        loginbox.geometry("250x100")
        FormLogin(loginbox)
