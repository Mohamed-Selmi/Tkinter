import json
from test import *
#Bechn thabet if user input matches requirements and the date is correct and make it a json
def turn_to_json(nom,prenom,email,jour,mois,anne):
    if verify_string(nom) and verify_string(prenom) and verify_email(email) and verify_date(jour,mois,anne): 
        student_string = f'{{"nom": "{nom}", "prenom": "{prenom}", "email": "{email}", "naissance": "{format_date(anne,mois,jour)}"}}'
        json_student=json.loads(student_string)
        return json_student
    else:
        return "wtf are you writing"
    
#insertion works!
def insert(cnx,student):
    try:
        sql= "INSERT INTO student(nom,prenom,email,naissance) values (%s,%s,%s,%s)"
        val=(student["nom"],student["prenom"],student["email"],student["naissance"])
        mycursor=cnx.cursor()
        mycursor.execute(sql,val)
        cnx.commit()
        return "input successful! Yohoo!"
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
#select all works

def show_all(cnx):
    sql="select * from student"
    mycursor=cnx.cursor()
    mycursor.execute(sql)
    result=mycursor.fetchall()
    l=[]
    for x in result:
        l.append(x)
    return l
#searches a student by id: works
def search(cnx,id):
        sql= "select * from student where id like {id1}".format(id1=id)
        mycursor=cnx.cursor()
        mycursor.execute(sql)
        result=mycursor.fetchone()
        
        if not result:
                return "mafamech"
        else:
                return result
def delete(cnx,id):
        sql= "Delete from student where id = {id1}".format(id1=id)
        mycursor=cnx.cursor()
        mycursor.execute(sql)
        result=mycursor.fetchone()
        
        if not result:
                return "mafamech"
        else:
                return "Deleted succesfully"
#works 
def update(cnx,id,student):
    sql="UPDATE student set nom=%s, prenom=%s, email=%s, naissance=%s where id=%s"
    val=(student["nom"],student["prenom"],student["email"],student["naissance"],id)
    mycursor=cnx.cursor()
    mycursor.execute(sql,val)
    cnx.commit()
    result=mycursor.fetchone()
        
    if not result:
            return "mafamech"
    else:
            return "Insertion successful"
