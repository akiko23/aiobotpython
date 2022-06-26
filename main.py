from datetime import datetime
from functions import *
from db import Database

database = Database("database.db")

database.add_column('n')

place = input("Введите место, которое посещали: ")
database.set_place(last_id=database.get_last_id(), place=place)

check_country(database=database, place=place)

time = input(f"Когда вы посещали {place}(формат ввода: dd.mm.yyyy  Пример: 24.02.2007)? ")
database.set_time(database.get_last_id(), time.split('.')[1])
database.check_month()


grade = int(input("На сколько бы оценили вашу поездку(от 1 до 5)? "))

if 5 >= grade >= 1:
    database.set_grade(database.get_last_id(), grade)
else:
    print("Такой оценки нет")


relax_category = input("Ваш отдых был активным или пассивным(1 - активным; 2 - пассивным)? ")

if relax_category == '1':
    database.set_act_or_pas_relax(database.get_last_id(), "active")

elif relax_category == '2':
    database.set_act_or_pas_relax(database.get_last_id(), "passive")

print(get_and_set_result(database=database))
