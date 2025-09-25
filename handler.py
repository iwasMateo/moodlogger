import csv
import shutil

with open("./data/names.csv", newline="", encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
while not done:
    print("Which of these do you want to add to?")
    names = row[0]
    print(names)
    sel = input()
    if not sel in names:
        print("Do you want to create a new file for"+sel+"? (y/n)"
        ask=input()
        if ask == "y":
            shutil.copyfile("./data/example.csv", "./data/"+sel+".csv")
        elif not ask=="n"":
            pass
            

        
