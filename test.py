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

def turnToDate(birthDay):
        try:
                birthDayArray=birthDay.split("-")
                year=int(birthDayArray[0])
                month=int(birthDayArray[1])
                day=int(birthDayArray[2])
                return (year,month,day) 
        except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")

def verify_date(birthday):
    (year,month,day)=turnToDate(birthday)
    test=True
    if day not in range (1,32):
        test=False
    if month not in range (1,13):
        test=False
    if year not in range(1945,2026):
        test=False
    return test
def format_date(date):
    (year,month,day)=turnToDate(date)
    return datetime.datetime(year,month,day)

def verify_student(student):

    return verify_string(student["nom"]) and verify_string(student["prenom"])and verify_email(student["email"]) and verify_date(student["mois"],)


