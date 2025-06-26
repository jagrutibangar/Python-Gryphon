import csv

with open("people.csv", "w", newline="") as myfile:
    writer = csv.writer(file)
    writer.writerow(["Name","Age"])
    writer.writerow(["Aaditi","20"])