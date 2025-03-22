import tkinter as tk
from tkinter import ttk
from sql_connection import *
from test import *
from sqlcommands import *
from Window1 import MainWindow
from login import Login
config=get_config()
connection = start_connection(config)
def main():
    root = tk.Tk()
    root.title("Gestion de bases des etudiants")
    root.geometry('1280x720')
   
    root.maxsize(1280,720)
    root.configure(background='#FFEAAE')
    app = Login(root,connection)
    root.mainloop()

if __name__ == '__main__':
    main()

close_connection(connection)
