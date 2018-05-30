import sqlite3
import os

db_path='C:\\Users\\USER\\Desktop\\KURSOVIK\\CHERNOVIK'
db_file='database.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()

userrail_2=input("Класс вагона: ")
userrail2_2=''.join(userrail_2)
userrail3_2=userrail2_2.title()
testkupe_2="Купе"
testplaz_2="Плацкарт"

usernumb_2=input("Номер места: ")
usernumb2_2=''.join(usernumb_2)
usernumb3_2=int(usernumb2_2)
if usernumb3_2 in range(0,11):
	print('')
else:
	print("Вводимое число мест должно быть от 0 до 10")

if userrail3_2 in testplaz_2:
    if usernumb3_2==1:
        cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=1""")
    elif usernumb3_2==2:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=2""")
    elif usernumb3_2==3:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=3""")
    elif usernumb3_2==4:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=4""")
    elif usernumb3_2==5:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=5""")
    elif usernumb3_2==6:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=6""")
    elif usernumb3_2==7:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=7""")
    elif usernumb3_2==8:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=8""")
    elif usernumb3_2==9:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=9""")
    elif usernumb3_2==10:
	    cur.execute("""UPDATE plaz SET numb_place='Это место уже забронировано' WHERE numb_place=10""")
    else:
	    print('Места забронированы')
else:
	os.startfile('C:\\Users\\USER\\Desktop\\KURSOVIK\\CHERNOVIK\\tickets3.py')

con.commit()
con.close()