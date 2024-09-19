#################################################
# Iterator
#################################################

txt = 'Hello Python'
iterator_txt = iter(txt)

H = next(iterator_txt)
print(H)

print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))
print(next(iterator_txt))


#################################################
# While
#################################################

number = 0

while number < 10:
    number += 0.5
    print(number)


print("Finished While Cycle")


counter = 0

while True:
    number = int(input("Enter a number: "))
    if number > 0:
        print(number)
        break

    counter += 1

    if counter == 5:
        break

print("While Finished")


number = 0

while True:

    if number == 5:
        number += 1
        continue

    if number == 10:
        break

    number += 1
    print(number)



number = 0

while number < 10:
    print(number)
    number += 1

    if number == 5:
        break
else:
    print("Else Block")




#################################################
# For
#################################################

range_number = [0, 1, 2, 3, 4]
iterator_range = iter(range_number)

i = next(iterator_range)
if i == 2:
    print(i)

i = next(iterator_range)
if i == 2:
    print(i)

i = next(iterator_range)
if i == 2:
    print(i)

i = next(iterator_range)
if i == 2:
    print(i)

i = next(iterator_range)
if i == 2:
    print(i)

for i in range(5, 10, 2):
    if i == 2:
        print(i)

txt = "Hello Python"

for char in txt:
    print(char)



#################################################
# Nested Cycles
#################################################


for i in range(5):
    for j in range(5):
        print(i, j)


number = 0

while number < 5:
    number1 = 0
    while number1 < 5:
        print(number, number1)
        number1 += 1
        break
    else:
        print("nested else")
    number += 1



#################################################
# random
#################################################

import random

random_number = random.random()
print(random_number)

random_integer = random.randint(1, 10)
print(random_integer)

random_range = random.randrange(1, 10)
print(random_range)
