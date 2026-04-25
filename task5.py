import csv
file = open('employees.csv', 'w')
writer = csv.writer(file)
writer.writerow(["name", "salary"])
writer.writerow(["Berik", 300000])
writer.writerow(["Serik", 400000])
writer.writerow(["Erik", 500000])
file.close()