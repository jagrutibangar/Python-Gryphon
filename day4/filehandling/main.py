import csv

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age"])
    writer.writerow(["Aaditi","20"])
    writer.writerow(["Jagruti","20"])
    writer.writerow(["Harsh","19"])