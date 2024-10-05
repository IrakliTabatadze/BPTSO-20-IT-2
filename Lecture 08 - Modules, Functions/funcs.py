print('Hello From Terminal')

import random
from faker import Faker

fake = Faker()
print(fake.name())


import test
from test import number1, number2

print(number1 + number2)

from testDirectory import different
print(different.diff_var)

from testDirectory.different import diff_var
print(diff_var)


##################################################
# Function
##################################################

def plus():
    return 10 + 15

added_number = plus()
print(added_number)

import random
rand_number = random.randint(1, 10)
print(rand_number)


def plus(a, b):
    # print(f'a = {a}')
    # print(f'b = {b}')
    return a + b

counter = 1
while counter <= 3:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))

    added_number = plus(number1, number2)
    print(f'added_number = {added_number}')
    counter += 1



def palyndrome(word):
    return word == word[::-1] # True/False


is_palyndrome1 = palyndrome('Python')
is_palyndrome2 = palyndrome('saas')

print(f'is_palyndrome1 is palyndrome? || {is_palyndrome1}')
print(f'is_palyndrome2 is palyndrome? || {is_palyndrome2}')

counter = 1
while counter <= 3:
    user_input = input('Please enter some word: ')

    is_palyndrome = palyndrome(user_input)

    if is_palyndrome:
        print(f'{user_input} is a palyndrome.')
    else:
        print(f'{user_input} is not a palyndrome.')

    counter += 1





def plus(a=25, b=10, c=0, d=0, e=0, f=0):
    print(f'c = {c}')
    print(f'd = {d}')
    return a + b, c - d, e * f


added_number = plus(10, 20, d=150, c=250)
print(added_number)



# def posArgs(a, *args, **kwargs):
#     print(args)
#     # for arg in args:
#     #     print(arg)
#     print(kwargs)
#
# posArgs(1,2,3,4, number1=150, number2=250)
