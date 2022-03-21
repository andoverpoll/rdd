import csv

numbers_array = []

with open('number_list.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        numbers_array.append(row)
    
