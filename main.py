import csv
from utils import openspace

openspace1=Openspace()

filename = "./utils/data.csv"
with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        openspace1.organize(row)
        #write your code here

openspace1.display()
