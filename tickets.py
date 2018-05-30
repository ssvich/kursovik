import sqlite3
import os
db_path='C:\\Users\\USER\\Desktop\\KURSOVIK\\CHERNOVIK'
db_file='database.db'
full_path=os.path.join(db_path,db_file)

sql="""
CREATE TABLE IF NOT EXISTS kupe(sort_place TEXT NOT NULL, numb_place INTEGER NOT NULL);
CREATE TABLE plaz (sort_place TEXT NOT NULL, numb_place INTEGER NOT NULL);
"""

con=sqlite3.connect(full_path)
cur=con.cursor()
cur.executescript(sql)
cur.close()
con.close()