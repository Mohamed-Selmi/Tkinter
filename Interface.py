from tkinter import *
from tkinter import ttk



def switchWindow(root,connection,originalWindow,newWindow):
    newWindow(root,connection)
    root.mainloop()
#def destroyWindow(root,connection,)