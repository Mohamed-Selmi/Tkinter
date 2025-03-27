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
        self.master.geometry('1280x720')
        self.master.maxsize(1280,720)
        self.mainframe=tk.Frame(self.master, width=1280, height=720,bg='#FFEAAE', relief="solid")
        self.mainframe.place(x=0,y=0)
        self.frame1=tk.Frame(self.mainframe, width=250, height=550,bg='#AFAAB9',borderwidth=2, relief="solid")
        self.frame1.place(x=1280-260,y=10)
        self.add_button=tk.Button(self.frame1,text="Add student",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=self.add_student)
        self.add_button.place(x=10,y=25,height=100,width=225)

        self.update_button=tk.Button(self.frame1,text="Update student",font=('Arial',15,"bold"),bg='#F39E60',borderwidth=2, relief="solid")
                                     #command=lambda: switchWindow(self.master,self.connection,MainWindow,Login))
        self.update_button.place(x=10,y=150,height=100,width=225)
        self.Delete_button=tk.Button(self.frame1,text="Delete student",font=('Arial',15,"bold"),bg='#FFDAB3',borderwidth=2, relief="solid",command=self.deleteStudent)  
        self.Delete_button.place(x=10,y=275,height=100,width=225)
        self.refresh_button=tk.Button(self.frame1,text="Refresh database",font=('Arial',15,"bold"),bg='#FADA7A',borderwidth=2, relief="solid",command=self.fetchData)  
        self.refresh_button.place(x=10,y=400,height=100,width=225)

        #make the birthdate into one input and use .spit("/") or .split("-")(function) and pass it to turntojson that way
        self.frame2=tk.Frame(self.mainframe, width=1000, height=420,bg='#197278',borderwidth=2, relief="solid")
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
        self.Birthday_label=tk.Label(self.frame2, text="Enter student's birthday Y-M-D:",font=('Arial',13,"bold"))
        self.Birthday_label.place(x=450,y=10)
        self.Bday=tk.Entry(self.frame2,width=50)
        self.Bday.place(x=450,y=50)
        self.Registration_label=tk.Label(self.frame2, text="Enter student's registration number:",font=('Arial',13,"bold"))
        self.Registration_label.place(x=450,y=100)
        self.Registration=tk.Entry(self.frame2,width=50)
        self.Registration.place(x=450,y=150)
        self.Specialty_label=tk.Label(self.frame2, text="Enter student's specialty:",font=('Arial',13,"bold"))
        self.Specialty_label.place(x=450,y=200)
        self.Specialty=ttk.Combobox(self.frame2,height = 10,width=50, values=('Informatique', 'Prepa', 'Architecture', 'Biochimie','Electrique'))
 
        self.Specialty.place(x=450,y=250)
        #show existing databse elements here
        self.frame3=tk.Frame(self.mainframe, width=1000, height=250,bg='#AFAAB9',borderwidth=2, relief="solid")
        self.frame3.place(x=10,y=720-260)
        self.studentTable=ttk.Treeview(self.frame3,columns= ("Firstname","Lastname","Email","Birthday","Specialty","Matricule"))
        self.studentTable.place(x=10,y=10)
        style = ttk.Style()
        style.configure("Treeview.Heading",font=('Arial',13,"bold"))
        self.studentTable.column("#0", width=0,anchor='center')
        self.studentTable.column("Firstname",  width=180,anchor='center')
        self.studentTable.column("Lastname", width=100,anchor='center')
        self.studentTable.column("Email",  width=180,anchor='center')
        self.studentTable.column("Birthday",  width=140,anchor='center')
        self.studentTable.column("Specialty", width=140,anchor='center')
        self.studentTable.column("Matricule", width=180,anchor='center')
        self.studentTable.heading("Firstname",  text="Firstname",anchor='center')
        self.studentTable.heading("Lastname", text="Lastname",anchor='center')
        self.studentTable.heading("Email",  text="Email")
        self.studentTable.heading("Birthday",  text="Birthday")
        self.studentTable.heading("Specialty", text="Specialty")
        self.studentTable.heading("Matricule", text="Matricule",anchor='center')
        self.studentTable.bind("<<TreeviewSelect>>",self.selectStudentItem)
    def fetchData(self):
        print('updating')
        for data in self.studentTable.get_children():
            self.studentTable.delete(data)

        for student in show_all(self.connection):
            self.studentTable.insert(parent='', index='end', iid=student, text="", values=(student), tag="row")
            self.studentTable.tag_configure('row', background='#EEEEEE', font=('Arial', 12,'bold'))
            self.studentTable.grid(row=8, column=6, columnspan=5, rowspan=11, padx=10, pady=20)
    def selectStudentItem(self,event):
        curItem = self.studentTable.focus()
        studentArr=self.studentTable.item(curItem)['values']
        firstname =studentArr[0]
        lastname = studentArr[1]
        email = studentArr[2]
        birthday = studentArr[3]
        specialty=studentArr[4]
        registration=studentArr[5]
        student=turn_to_json(firstname,lastname,email,birthday,specialty,registration)
        return student
    def deleteStudent(self):
            event="<<TreeviewSelect>>"
            student=self.selectStudentItem(event)
            print(student)
            delete(self.connection,student)
            self.fetchData()
    def test(self):
        firstname =self.Student_firstname.get()
        lastname = self.Student_lastname.get()
        email = self.Student_email.get()
        birthday = self.Bday.get()
        registration=self.Registration.get()
        specialty=self.Specialty.get()
        req=turn_to_json(firstname,lastname,email,birthday,specialty,registration)
        print(req)
    def add_student(self):
        try:
            firstname =self.Student_firstname.get()
            lastname = self.Student_lastname.get()
            email = self.Student_email.get()
            birthday = self.Bday.get()
            registration=self.Registration.get()
            specialty=self.Specialty.get()
            req=turn_to_json(firstname,lastname,email,birthday,specialty,registration)
            insert(self.connection,req)
            self.fetchData()
        except:
            MessageBox.showinfo("ALERT", "Please verify input")
        
    #The main frame widget wraps around all the rest, and destroying it fixed any issue I had with navigating between pages.
    def closeWindow(self):
        self.mainframe.destroy()
        switchWindow(self.master,self.connection,Login) 
  

class Login:
    def __init__(self,master,connection):
        self.connection=connection
        self.master = master
        self.master.geometry('500x500')
        self.master.maxsize(500,500)
        self.frame1=tk.Frame(self.master, width=350, height=480,bg='#197278',borderwidth=2, relief="solid")
        self.frame1.place(x=75,y=10)
        self.add_button=tk.Button(self.frame1,text="Login",font=('Arial',15,"bold"),bg='#F0A04B',borderwidth=2, relief="solid",command=self.closeWindow)
                                  #command=lambda: [switchWindow(self.master,self.connection,Login,MainWindow),self.frame1.destroy])
        self.add_button.place(x=50,y=480-100,height=50,width=250)
        self.login_label= tk.Label(self.frame1, text="Enter your name",font=('Arial',13,"bold"))
        self.login_label.place(x=100,y=35)
        self.admin_name=tk.Entry(self.frame1,width=50)
        self.admin_name.place(x=15,y=75) 
        self.password_label= tk.Label(self.frame1, text="Enter your password",font=('Arial',13,"bold"))
        self.password_label.place(x=100,y=125)
        self.admin_password=tk.Entry(self.frame1,width=50)
        self.admin_password.place(x=15,y=165)         
    #Destroys the frame before loading the main window. Gets rids of the lingering login tab in the background after switching windows. 
    def closeWindow(self):
        self.frame1.destroy()
        switchWindow(self.master,self.connection,MainWindow)






def switchWindow(root,connection,newWindow):
    newWindow(root,connection)
    root.mainloop()