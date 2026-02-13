import csv

openspace1=Openspace()

filename = "./utils/data.csv"
with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        openspace1.organize(row)
        #write your code here

with open("colleagues.csv", "w", encoding="utf-8-sig") as file:
    file.write("New Colleagues\n")
    for name in new_collegues:
        file.write(name + "\n")
