import csv
file1 = open('employees.csv', 'r')
reader = csv.reader(file1)
file2 = open('employees_updated.csv', 'w')
writer = csv.writer(file2)

header = next(reader)
header.append("annual_salary")
writer.writerow(header)

for row in reader:
    if len(row) > 1:
        salary = int(row[1])
        annual_salary = salary * 12
        row.append(annual_salary)
        writer.writerow(row)
file1.close()
file2.close()