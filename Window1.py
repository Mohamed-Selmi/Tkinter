import tkinter as tk
import tkinter as tk
from tkinter import ttk
from sql_connection import *

from test import *
from sqlcommands import *
class MainWindow:
    def __init__(self,master,connection):
        self.connection=connection
        self.master = master
        self.frame1=tk.Frame(self.master, width=250, height=550,bg='#AFAAB9',borderwidth=2, relief="solid")
        self.frame1.place(x=1280-260,y=10)
        self.add_button=tk.Button(self.frame1,text="Add student",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=self.add_student)
        self.add_button.place(x=10,y=25,height=100,width=225)

        self.update_button=tk.Button(self.frame1,text="Update student",font=('Arial',15,"bold"),bg='#F39E60',borderwidth=2, relief="solid")
        self.update_button.place(x=10,y=150,height=100,width=225)
        self.Delete_button=tk.Button(self.frame1,text="Delete student",font=('Arial',15,"bold"),bg='#FFDAB3',borderwidth=2, relief="solid")  
        self.Delete_button.place(x=10,y=275,height=100,width=225)
        self.refresh_button=tk.Button(self.frame1,text="Refresh database",font=('Arial',15,"bold"),bg='#FADA7A',borderwidth=2, relief="solid")  
        self.refresh_button.place(x=10,y=400,height=100,width=225)


        self.frame2=tk.Frame(self.master, width=1000, height=420,bg='#197278',borderwidth=2, relief="solid")
        self.frame2.place(x=10,y=10)
        self.firstname_label= tk.Label(self.frame2, text="Enter student's first name",font=('Arial',13,"bold"))
        self.firstname_label.place(x=20,y=10)
        self.Student_firstname=tk.Entry(self.frame2,width=50)
        self.Student_firstname.place(x=10,y=50)
        self.Lastname_label = tk.Label(self.frame2, text="Enter student's last name:",font=('Arial',13,"bold"))
        self.Lastname_label.place(x=20,y=100)
        self.Student_lastname=tk.Entry(self.frame2,width=50)
        self.Student_lastname.place(x=10,y=150)
        self.Email_label = tk.Label(self.frame2, text="Enter student's email address:",font=('Arial',13,"bold"))
        self.Email_label.place(x=10,y=200)
        self.Student_email=tk.Entry(self.frame2,width=50)
        self.Student_email.place(x=10,y=250)
        self.Birthday_label=tk.Label(self.frame2, text="Enter student's birth day:",font=('Arial',13,"bold"))
        self.Birthday_label.place(x=450,y=10)
        self.Day=tk.Entry(self.frame2,width=50)
        self.Day.place(x=450,y=50)
        self.Birthmonth_label=tk.Label(self.frame2, text="Enter student's birth month:",font=('Arial',13,"bold"))
        self.Birthmonth_label.place(x=450,y=100)
        self.Month=tk.Entry(self.frame2,width=50)
        self.Month.place(x=450,y=150)
        self.Birthyear_label=tk.Label(self.frame2, text="Enter student's birth year:",font=('Arial',13,"bold"))
        self.Birthyear_label.place(x=450,y=200)
        self.Year=tk.Entry(self.frame2,width=50)
        self.Year.place(x=450,y=250)
        self.frame3=tk.Frame(self.master, width=1000, height=250,bg='#AFAAB9',borderwidth=2, relief="solid")
        self.frame3.place(x=10,y=720-260)
    def test(self):
        nom = self.Student_lastname.get()
        prenom=self.Student_firstname.get()
        email = self.Student_email.get()
        day = int(self.Day.get())
        month=int(self.Month.get())
        year=int(self.Year.get())
        req=turn_to_json(nom,prenom,email,day,month,year)
        print(req)
    def add_student(self):
        try:
            nom =  self.Student_lastname.get()
            prenom=self.Student_firstname.get()
            email = self.Student_email.get()
            day = int(self.Day.get())
            month=int(self.Month.get())
            year=int(self.Year.get())
            req=turn_to_json(nom,prenom,email,day,month,year)
            return insert(self.connection,req)
        except:
            MessageBox.showinfo("ALERT", "Please verif input")
    


