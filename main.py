import csv
from utils import openspace, table

table1=table.Table(seats=[table.Seat(free=True) for _ in range(4)])
table2=table.Table(seats=[table.Seat(free=True) for _ in range(4)])
table3=table.Table(seats=[table.Seat(free=True) for _ in range(4)])
table4=table.Table(seats=[table.Seat(free=True) for _ in range(4)])
table5=table.Table(seats=[table.Seat(free=True) for _ in range(4)])
table6=table.Table(seats=[table.Seat(free=True) for _ in range(4)])

openspace1=openspace.Openspace(tables=[table1, table2, table3, table4, table5, table6])

filename = "./utils/data.csv"
with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        openspace1.organize(row)
        #write your code here

openspace1.display()

openspace1.store("colleagues.csv")