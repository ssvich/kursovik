import sqlite3
import os
db_path='C:\\Users\\USER\\Desktop\\KURSOVIK\\CHERNOVIK'
db_file='database.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()

datakupe=[{"sort":'Верхнее' , "numb": 1 }, {"sort":'Нижнее' , "numb": 2 }, {"sort":'Верхнее' , "numb": 3 }, {"sort":'Нижнее' , "numb": 4 }, {"sort":'Верхнее' , "numb": 5 }, {"sort":'Нижнее' , "numb": 6 }, {"sort":'Верхнее' , "numb": 7 }, {"sort":'Нижнее' , "numb": 8 }, {"sort":'Верхнее' , "numb": 9 }, {"sort":'Нижнее' , "numb": 10 }]
dataplaz=[{"sort":'Верхнее' , "numb": 1 }, {"sort":'Нижнее' , "numb": 2 }, {"sort":'Верхнее' , "numb": 3 }, {"sort":'Нижнее' , "numb": 4 }, {"sort":'Верхнее' , "numb": 5 }, {"sort":'Нижнее' , "numb": 6 }, {"sort":'Верхнее' , "numb": 7 }, {"sort":'Нижнее' , "numb": 8 }, {"sort":'Верхнее' , "numb": 9 }, {"sort":'Нижнее' , "numb": 10 }]

sql1="""INSERT INTO kupe VALUES (:sort,:numb)"""
sql2="""INSERT INTO plaz VALUES (:sort,:numb) """

cur.executemany(sql1,datakupe)
cur.executemany(sql2,dataplaz)
con.commit()
cur.close()
con.close()