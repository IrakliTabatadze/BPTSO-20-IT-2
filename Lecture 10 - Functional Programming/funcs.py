############################################
# Lamba Functions
############################################

def test(x):
    return x


print(test("Hello"))

return_lambda = lambda x: x
print(return_lambda('Hello Lambda Function'))



def plus(x, y):
    return x + y


plus_func = lambda x=10, y=15: x + y

print(plus_func(y=10, x=20))
print(plus_func(10, 15))
print(plus_func(15))



is_digit = lambda user_inp: user_inp.isdigit() and len(user_input) == 11

user_input = input('Please enter your private number: ')

print(is_digit(user_input))



private_number_lst = ['10101001', 'a123123', 'asasdfasdf', '124124', '125125125']

new_lst = [(lambda pr_number: pr_number if pr_number.isdigit() else '')(info) for info in private_number_lst]

print(new_lst)

for func in new_lst:
    print(func())


#####################################################
# High Priority Functions
#####################################################

from functools import partial, reduce

def power(x, y):
    return x ** y


power_number = partial(power, x=2)
print(power_number(x=2,y=10))
print(power_number(x=2,y=50))
print(power_number(x=2,y=100))



lst = [10, 11, 5, 125, 26, 24, 25, 15]
lst = [10, 5, 20, 100]
sum_of_number = reduce(lambda a, b: a * b, lst)
print(sum_of_number)



lst = [10, 11, 5, 125, 26, 24, 25, 15]
max_value = reduce(lambda a, b: a if a < b else b, lst)
print(max_value)

factorial = reduce(lambda x, y: x * y, range(1, 6))
print(factorial)




names_list = ['john', 'joe', 'mary', 'kate', 'james', 'sean']
result = list(map(str.capitalize, names_list))
print(result)



####################################################
# Try Except
####################################################

try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))

    print(number1 / number2)
except ValueError as e:
    print('Please Input Valid Integer')
    # print(e)
except ZeroDivisionError as e:
    print('Cannot divide by zero, please try again')
except Exception as e:
    print(e)
else:
    print('Everything Finished Successfully')
finally:
    print('Goodbye')


