
with open('test.csv', 'r') as csv_file:

    headers = csv_file.readline()
    for line in csv_file.readlines():
        print(line.replace('\n', '').split(';'))



##################################################
# Read CSV
##################################################

import csv

with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    headers = next(csv_reader)

    print(headers)

    for row in csv_reader:
        print(row)

    new_info_lst = []

    for row in csv_reader:
        full_info = ''
        for i in range(len(row)):
            # print(i)
            if i == 0:
                full_info += f'first_name: {row[i]} '
            elif i == 1:
                full_info += f'last_name: {row[i]}\n'
            new_info_lst.append(full_info)

    headers.pop()

with open('new_file.txt', 'w') as file:
    file.writelines(headers)

    file.writelines(new_info_lst)



with open('test1.csv', 'r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)

    for row in csv_dict_reader:
        print(row)




##################################################
# Write CSV
##################################################


import csv

headers = ['first_name', 'last_name', 'occupation', 'age']

info = [
    ['John', '', '', 25],
    ['Kate', 'Johnson', 'Doctor', 26],
    ['Anna', 'Smith', 'Accountant', 27]
]

with open('test3.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter='\t')

    csv_writer.writerow(headers)

    csv_writer.writerows(info)


with open('test3.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for row in csv_reader:
        print(row)


info = [
    {'first_name': 'John', 'age': 25},
    {'last_name': 'Johnson', 'first_name': 'Kate', 'occupation': 'Doctor', 'age': '25'},
    {'first_name': 'Anna', 'last_name': 'Smith', 'occupation': 'Accountant', 'age': '26'},
]


with open('test4.csv', 'w', newline='') as csv_file:
    csv_dict_writer = csv.DictWriter(csv_file, fieldnames=headers)

    csv_dict_writer.writeheader()

    csv_dict_writer.writerows(info)