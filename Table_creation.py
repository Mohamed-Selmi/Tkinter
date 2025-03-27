from mysql.connector import errorcode
from sql_connection import *
import mysql.connector
DB_NAME = 'students'
config=get_config()
cnx=start_connection(config)

mycursor=cnx.cursor()
mycursor.execute("CREATE TABLE student (id int primary key AUTO_INCREMENT,firstname varchar(50) NOT NULL, lastname varchar(50) NOT NULL,"
" email varchar(50) NOT NULL, birthday Date NOT NULL,specialty varchar(50) NOT NULL,matricule varchar(50) NOT NULL UNIQUE)")
#mycursor.execute("CREATE TABLE Admin (id int primary key AUTO_INCREMENT,nom varchar(50), password varchar(50) NOT NULL)")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x,"table")

"""def create_table(tablename):
    if mycursor."""