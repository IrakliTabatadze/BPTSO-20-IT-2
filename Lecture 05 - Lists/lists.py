############################################
# ReGex
############################################
import re

txt = 'Python is the best programming language'

regex = re.compile(r'[aeiou]')
pattern = r'p.*o'
matches = re.findall(pattern, txt)
print(matches)

txt = re.sub(pattern, '{Changed Information}', txt)
print(txt)

matches = re.match(regex, txt)
print(matches)


splited = regex.split(txt)
print(splited)


############################################
# Lists
############################################

empty_list1 = []
empty_list2 = list()
print(empty_list1)
print(empty_list2)


hobbies = ['Programming', 'Music', 'Drinking', 'Programming', 'Music', 'Drinking', 10, 5.5, True, False]
hobbies2 = ['Programming', 'Music', 'Drinking']

print(hobbies + hobbies2)
print(hobbies * 3)

print(hobbies[0])
print(hobbies[-1])
print(hobbies[1:4])
print(hobbies[:4])
print(hobbies[1:])


print('a' in hobbies)
print('Programming' not in hobbies)


############################################
# Lists Methods
############################################

hobbies = ['Programming', 'Music', 'Drinking', 'Programming', 'Music', 'Drinking', 10, 5.5, True, False]

hobbies.append("New Information")
hobbies.insert(2, 'Inserted Information')
print(hobbies)

hobbies.clear()
hobbies.remove('Programming')

count_programming = hobbies.count('Programming')
for _ in range(count_programming):
    hobbies.remove('Programming')

popped_item = hobbies.pop(2)
print(hobbies)
print(popped_item)

hobbies2 = hobbies.copy()
hobbies.clear()
print(hobbies)
print(hobbies2)


lst = [1, 2, 12, 4, 10, 6, 7, 8, 9]
lst.sort(reverse=True)
print(lst)
lst.reverse()
print(lst)
customer = [[1, 'John', 'Doe'], [2, 'Kate', 'Doe']]



hobbies = ['Programming', 'Music', 'Drinking', 'Programming', 'Music', 'Drinking', 10, 5.5, True, False]
other_hobbies = [hobby for hobby in hobbies if isinstance(hobby, str)]
other_hobbies = [i for i in range(1, 11)]

for hobby in hobbies:
    if isinstance(hobby, str):
        other_hobbies.append(hobby)


for i in range(1, 11):
    other_hobbies.append(i)

print(other_hobbies)


############################################
# Matrix
############################################

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_index_1 = matrix[1][1]
print(matrix_index_1)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'i = {i}, j = {j}, matrix[i][j] = {matrix[i][j]}')
