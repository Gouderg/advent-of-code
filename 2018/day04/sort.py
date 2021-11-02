from datetime import MAXYEAR, datetime
import re

def sort_date(data):
    for i in range(1, len(data)):
        x = data[i]
        x_date = datetime.strptime(data[i].split('] ')[0].replace('[', ''), "%Y-%m-%d %H:%M")
        j = i
        j_date = datetime.strptime(data[j - 1].split('] ')[0].replace('[', ''), "%Y-%m-%d %H:%M")
        
        while j > 0 and j_date > x_date:
            data[j] = data[j -1]
            j -= 1
            j_date = datetime.strptime(data[j - 1].split('] ')[0].replace('[', ''), "%Y-%m-%d %H:%M")
        data[j] = x
    return data

# Extract data.
data = []
with open("input.txt", 'r') as file:
    for row in file:
        data.append(row.replace('\n', ''))

# Sort by date
data = sort_date(data)

# Write data.
with open('input_sort.txt', 'w') as file:
    for row in data:
        file.write(row+'\n')

