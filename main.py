filename = "./utils/data.xlsx"
with open(filename, "r") as my_file:
    for line in my_file:
        #write your code here

with open("colleagues.csv", "w", encoding="utf-8-sig") as file:
    file.write("New Colleagues\n")
    for name in new_collegues:
        file.write(name + "\n")
