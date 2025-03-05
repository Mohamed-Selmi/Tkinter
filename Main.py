import tkinter as tk
from tkinter import ttk
from sql_connection import *
from test import *
from sqlcommands import *

#config=get_config()
#connection = start_connection(config)
root = tk.Tk()
root.title("Gestion de bases des etudiants")
root.geometry('1280x720')
root.minsize(1280,720)
root.maxsize(1280,720)
root.configure(background='#FFEAAE')
frame1=tk.Frame(root, width=250, height=550,bg='#AFAAB9',borderwidth=2, relief="solid")
frame1.place(x=1280-260,y=10)
add_button=tk.Button(frame1,text="Add student",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid")
add_button.place(x=10,y=25,height=100,width=225)

update_button=tk.Button(frame1,text="Update student",font=('Arial',15,"bold"),bg='#F39E60',borderwidth=2, relief="solid")
update_button.place(x=10,y=150,height=100,width=225)
Delete_button=tk.Button(frame1,text="Delete student",font=('Arial',15,"bold"),bg='#FFDAB3',borderwidth=2, relief="solid")  
Delete_button.place(x=10,y=275,height=100,width=225)
refresh_button=tk.Button(frame1,text="Refresh database",font=('Arial',15,"bold"),bg='#FADA7A',borderwidth=2, relief="solid")  
refresh_button.place(x=10,y=400,height=100,width=225)

















#





#hello=("mohamed","amine","HELLO@gmail.com",15,8,2022)
#print(search(connection,11))
#req=turn_to_json(*hello)
#insert(connection,req)
#print(delete(connection,4))
#print(update(connection,22,req))
#print(show_all(connection))

#close_connection(connection)
root.mainloop()