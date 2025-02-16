from tkinter import *
from tkinter import ttk
from sql_connection import *
from test import *
from sqlcommands import *

config=get_config()
connection = start_connection(config)
hello=("mohamed","amine","HELLO@gmail.com",15,8,2022)
#print(search(connection,11))
req=turn_to_json(*hello)
#insert(connection,req)
#print(delete(connection,4))
print(update(connection,22,req))
#print(show_all(connection))

close_connection(connection)