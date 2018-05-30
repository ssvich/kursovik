import sqlite3
import os

db_path='C:\\Users\\USER\\Desktop\\KURSOVIK\\CHERNOVIK'
db_file='database.db'
full_path=os.path.join(db_path,db_file)

con=sqlite3.connect(full_path)
cur=con.cursor()

userrail=input("Класс вагона: ")
userrail2=''.join(userrail)
userrail3=userrail2.title()
testkupe="Купе"
testplaz="Плацкарт"


usernumb=input("Номер места: ")
usernumb2=''.join(usernumb)
usernumb3=int(usernumb2)
if usernumb3 in range(0,11):
	print('')
else:
	print("Вводимое число мест должно быть от 0 до 10")

if userrail3 in testkupe:
    if usernumb3==1:
        cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=1""")
    elif usernumb3==2:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=2""")
    elif usernumb3==3:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=3""")
    elif usernumb3==4:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=4""")
    elif usernumb3==5:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=5""")
    elif usernumb3==6:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=6""")
    elif usernumb3==7:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=7""")
    elif usernumb3==8:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=8""")
    elif usernumb3==9:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=9""")
    elif usernumb3==10:
	    cur.execute("""UPDATE kupe SET numb_place='Это место уже забронировано' WHERE numb_place=10""")
    else:
	    print('Места забронированы')
else:
	os.startfile('C:\\Users\\USER\\Desktop\\KURSOVIK\\CHERNOVIK\\tickets4.py')


con.commit() #сохраняет изменения
con.close() #закрывает объект-курсор и соединение

#if userrail3 in testplaz:
#	os.startfile('C:\\Users\\USER\\Desktop\\KURSOVIK\\CHERNOVIK\\tickets4.py')