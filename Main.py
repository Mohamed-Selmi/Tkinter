import tkinter as tk
from tkinter import ttk
from sql_connection import *
from test import *
from sqlcommands import *

config=get_config()
connection = start_connection(config)
def test():
    nom = Student_lastname.get()
    prenom=Student_firstname.get()
    email = Student_email.get()
    day = int(Day.get())
    month=int(Month.get())
    year=int(Year.get())
    req=turn_to_json(nom,prenom,email,day,month,year)
    print(req)
def add_student():
    nom = Student_lastname.get()
    prenom=Student_firstname.get()
    email = Student_email.get()
    day = int(Day.get())
    month=int(Month.get())
    year=int(Year.get())
    req=turn_to_json(nom,prenom,email,day,month,year)
    return insert(connection,req)


root = tk.Tk()
root.title("Gestion de bases des etudiants")
root.geometry('1280x720')
root.minsize(1280,720)
root.maxsize(1280,720)
root.configure(background='#FFEAAE')
frame1=tk.Frame(root, width=250, height=550,bg='#AFAAB9',borderwidth=2, relief="solid")
frame1.place(x=1280-260,y=10)
add_button=tk.Button(frame1,text="Add student",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=add_student)
add_button.place(x=10,y=25,height=100,width=225)

update_button=tk.Button(frame1,text="Update student",font=('Arial',15,"bold"),bg='#F39E60',borderwidth=2, relief="solid")
update_button.place(x=10,y=150,height=100,width=225)
Delete_button=tk.Button(frame1,text="Delete student",font=('Arial',15,"bold"),bg='#FFDAB3',borderwidth=2, relief="solid")  
Delete_button.place(x=10,y=275,height=100,width=225)
refresh_button=tk.Button(frame1,text="Refresh database",font=('Arial',15,"bold"),bg='#FADA7A',borderwidth=2, relief="solid")  
refresh_button.place(x=10,y=400,height=100,width=225)


frame2=tk.Frame(root, width=1000, height=420,bg='#197278',borderwidth=2, relief="solid")
frame2.place(x=10,y=10)
firstname_label= tk.Label(frame2, text="Enter student's first name",font=('Arial',13,"bold"))
firstname_label.place(x=20,y=10)
Student_firstname=tk.Entry(frame2,width=50)
Student_firstname.place(x=10,y=50)
Lastname_label = tk.Label(frame2, text="Enter student's last name:",font=('Arial',13,"bold"))
Lastname_label.place(x=20,y=100)
Student_lastname=tk.Entry(frame2,width=50)
Student_lastname.place(x=10,y=150)
Email_label = tk.Label(frame2, text="Enter student's email address:",font=('Arial',13,"bold"))
Email_label.place(x=10,y=200)
Student_email=tk.Entry(frame2,width=50)
Student_email.place(x=10,y=250)
Birthday_label=tk.Label(frame2, text="Enter student's birth day:",font=('Arial',13,"bold"))
Birthday_label.place(x=450,y=10)
Day=tk.Entry(frame2,width=50)
Day.place(x=450,y=50)
Birthmonth_label=tk.Label(frame2, text="Enter student's birth month:",font=('Arial',13,"bold"))
Birthmonth_label.place(x=450,y=100)
Month=tk.Entry(frame2,width=50)
Month.place(x=450,y=150)
Birthyear_label=tk.Label(frame2, text="Enter student's birth year:",font=('Arial',13,"bold"))
Birthyear_label.place(x=450,y=200)
Year=tk.Entry(frame2,width=50)
Year.place(x=450,y=250)
frame3=tk.Frame(root, width=1000, height=250,bg='#AFAAB9',borderwidth=2, relief="solid")
frame3.place(x=10,y=720-260)














#





#hello=("mohamed","amine","HELLO@gmail.com",15,8,2022)
#print(search(connection,11))
#req=turn_to_json(*hello)
#insert(connection,req)
#print(delete(connection,4))
#print(update(connection,22,req))
#print(show_all(connection))

root.mainloop()
close_connection(connection)
