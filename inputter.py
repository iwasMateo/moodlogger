import csv

with open("./data/example.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

names = row[0]
