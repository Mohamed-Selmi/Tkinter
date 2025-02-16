import datetime
def verify_email(a):
    test=False
    if '@' in a:
        test=True
    l=[".com",".fr",".tn"]
    domain=["gmail","outlook","poyltechnicien","hotmail"]
    for i in l:
        if i in a:
            test=True
            break
        else:
            test=False
    for j in domain:
        if j in a:
            test=True
            break
        else:
            test=False
    return test
    

def verify_string(a):
    return a.isalpha() and len(a)<50


def verify_date(j,m,a):
    test=True
    if j not in range (1,32):
        test=False
    if m not in range (1,13):
        test=False
    if a not in range(1945,2026):
        test=False
    return test
def format_date(a,m,j):
    return datetime.datetime(a,m,j)

def verify_student(student):

    return verify_string(student["nom"]) and verify_string(student["prenom"])and verify_email(student["email"]) and verify_date(student["mois"],)

 
def vera(nom,prenom,email,jour,mois,anne):
    return verify_string(nom) and verify_string(prenom) and verify_email(email) and verify_date(jour,mois,anne)

