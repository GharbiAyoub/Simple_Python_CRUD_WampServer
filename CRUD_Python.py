import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="", db="test")

mycursor = conn.cursor()
myQueryCreate = """Create Table Names(
        id int primary Key AUTO_INCREMENT,
        name varchar(20)
    )"""

myQueryInsert = """ 
     Insert into names (name)
     values('Gharbi')
"""

myQueryDelete = """ 
     Delete From Names where id = 1
"""

myQueryUpdate = """ 
     Update Names set name= 'Ayoub' where id = 2
"""

myQuerySelect = """
    Select * from Names
"""
#mycursor.execute(myQueryInsert)
#mycursor.execute(myQueryUpdate)
mycursor.execute(myQuerySelect)

print(mycursor.fetchall(),end="\n")
