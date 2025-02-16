import csv

csv_file = open('test.csv', 'w')

writer = csv.writer(csv_file, delimiter =';')

header = ['Last name', 'First name', 'Age', 'Country']
writer.writerow(header)
data = [
    ['Smith', 'John', '35', 'USA'],
    ['Shiva', 'Gaikwad', '12', 'India']
]
# writer.writerow(header)

writer.writerows(data)

csv_file.close()