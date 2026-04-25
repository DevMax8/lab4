import csv
file = open('employees.csv', 'r')
reader = csv.reader(file)
next(reader)
total = 0
count = 0
for row in reader:
    if len(row) > 1:
        total += int(row[1])
        count += 1
print(total / count)
file.close()