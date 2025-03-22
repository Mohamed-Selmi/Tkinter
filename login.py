import tkinter as tk
import tkinter as tk
from tkinter import ttk
from sql_connection import *
from test import *
from sqlcommands import *
class Login:
    def __init__(self,master,connection):
        self.connection=connection
        self.master = master
        self.master.geometry('500x500')
        self.frame1=tk.Frame(self.master, width=250, height=550,bg='#AFAAB9',borderwidth=2, relief="solid")
