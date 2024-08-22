import csv 

print ("Reading csv file>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
with open('sample_data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print ("Reading file line by line>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
       
with open('sample_data.csv','r') as file:
    for line in file:
        print(line.strip())