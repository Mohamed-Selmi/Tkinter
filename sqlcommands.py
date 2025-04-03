import json
from test import *
import tkinter.messagebox as MessageBox

#Bechn thabet if user input matches requirements and the date is correct and make it a json
def turn_to_json(firstname,lastname,email,birthDay,specialty,registration):
    if verify_string(firstname) and verify_string(lastname) and verify_email(email) and verify_date(birthDay): #and checkUniqueStudent(registration): 
        student_string = f'{{"firstname": "{firstname}", "lastname": "{lastname}", "email": "{email}", "birthday": "{format_date(birthDay)}","specialty":"{specialty}","matricule":"{registration}"}}'
        json_student=json.loads(student_string)
        return json_student
    else:
        return "wtf are you writing"
    
#insertion works!
def insert(connection,student):
    try:
        sql= "INSERT INTO student(firstname,lastname,email,birthday,specialty,matricule) values (%s,%s,%s,%s,%s,%s)"
        val=(student["firstname"],student["lastname"],student["email"],student["birthday"],student["specialty"],student["matricule"])
        mycursor=connection.cursor()
        mycursor.execute(sql,val)
        connection.commit()
        return True
    except Exception as err:
        print(f"Unexpaected {err=}, {type(err)=}")
        MessageBox.showinfo("ALERT", f"Unexpaected {err[0]}, {type(err)=}")
#select all works

def show_all(connection):
    sql="select firstname,lastname,email,birthday,specialty,matricule from student"
    mycursor=connection.cursor()
    mycursor.execute(sql)
    result=mycursor.fetchall()
    l=[]
    for x in result:
        l.append(x)
    return l
#searches a student by id: works
def search(connection,id):
        sql= "select * from student where id like {id1}".format(id1=id)
        mycursor=connection.cursor()
        mycursor.execute(sql)
        result=mycursor.fetchone()
        
        if not result:
                return "mafamech"
        else:
                return result
def delete(connection,student):
        mat=student["matricule"]
        sql= "DELETE FROM student WHERE matricule = %s"
        val=(mat,)
        mycursor=connection.cursor()
        mycursor.execute(sql,val)
        result=mycursor.fetchone()
        print(result)
        if not result:
                return "mafamech"
        else:
                return "Deleted succesfully"
#works

def update(connection,matricule,student):
    sql="UPDATE student set firstname=%s, lastname=%s, email=%s, birthday=%s,specialty=%s,matricule=%s where matricule=%s"
    val=(student["firstname"],student["lastname"],student["email"],student["birthday"],student["specialty"],student["matricule"],matricule)
    mycursor=connection.cursor()
    mycursor.execute(sql,val)
    connection.commit()
    result=mycursor.fetchone()
        
    if not result:
            return "mafamech"
    else:
            return "Insertion successful"
def loginAdmin(connection,name,password):
    sql="select * from admin where nom=%s and password=%s"
    val=(name,password)
    mycursor=connection.cursor(buffered=True)
    mycursor.execute(sql,val)
    connection.commit()
    result=mycursor.fetchone()
    print(result)
    if result==None:
            return False
    else:
            return True
def checkUniqueStudent(connection,matricule):
        sql="select * from students where matricule=%s"
        val=(matricule)
        mycursor=connection.cursor()
        mycursor.execute(sql,val)
        connection.commit()
        result=mycursor.fetchone()
        if not result:
            return True
        else:
            return False
        


def registerAdmin(connection,name,password):
    try:
        sql="insert into Admin(nom,password) values (%s,%s)"
        val=(name,password)
        mycursor=connection.cursor()
        mycursor.execute(sql,val)
        connection.commit()
        return True
    except Exception as err:
        print(f"Unexpaected {err=}, {type(err)=}")
        MessageBox.showinfo("ALERT", f"Unexpaected {err[0]}, {type(err)=}")