from tkinter import *
from tkinter import ttk
def switchWindow(root,connection,window):
    window(root,connection)
    root.mainloop()