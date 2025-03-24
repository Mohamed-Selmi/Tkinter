import tkinter as tk
import tkinter as tk
from tkinter import ttk
from sql_connection import *
from test import *
from Window1 import MainWindow
from Interface import switchWindow
from sqlcommands import *
class Login:
    def __init__(self,master,connection):
        self.connection=connection
        self.master = master
        self.master.geometry('500x500')
        self.master.maxsize(500,500)
        self.frame1=tk.Frame(self.master, width=350, height=480,bg='#197278',borderwidth=2, relief="solid")
        self.frame1.place(x=75,y=10)
        self.add_button=tk.Button(self.frame1,text="Login",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=lambda: switchWindow(self.master,self.connection,MainWindow))
        self.add_button.place(x=50,y=480-100,height=50,width=250)
        self.login_label= tk.Label(self.frame1, text="Enter your name",font=('Arial',13,"bold"))
        self.login_label.place(x=100,y=35)
        self.admin_name=tk.Entry(self.frame1,width=50)
        self.admin_name.place(x=15,y=75) 
        self.password_label= tk.Label(self.frame1, text="Enter your password",font=('Arial',13,"bold"))
        self.password_label.place(x=100,y=125)
        self.admin_password=tk.Entry(self.frame1,width=50)
        self.admin_password.place(x=15,y=165)         
    '''def verify_login(self):
            try:
                nom =  self.admin_name.get()
                password=self.admin_password.get()
                return loadPage(master,connection)
            except:
                MessageBox.showinfo("ALERT", "Please verify login/password")   '''
