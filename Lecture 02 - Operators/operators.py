#######################################################
# Arithmetic Operators
#######################################################

number1 = 10
number2 = 3

print("number1 + number2 =", number1 + number2)
print("number1 - number2 =", number1 - number2)
print("number1 * number2 =", number1 * number2)
print("number1 / number2 =", number1 / number2)
print("number1 // number2 =", number1 // number2)
print("number1 % number2 =", number1 % number2)
print("number1 ** number2 =", number1 ** number2)


#######################################################
# Assignment Operators
#######################################################

number = 10
number = number + 10
number += 10
print(number)


number1 = int(input("Enter a number: "))
number1 += 10
print(number1)


number2 = int(input("Enter a number: "))
number2 -= 10
print(number2)

number3 = int(input("Enter a number: "))
number3 *= 10
print(number3)

number4 = int(input("Enter a number: "))
number4 /= 10
print(number4)


number5 = int(input("Enter a number: "))
number5 //= 10
print(number5)

number6 = int(input("Enter a number: "))
number6 %= 10
print(number6)

number7 = int(input("Enter a number: "))
number7 **= 10
print(number7)


#######################################################
# Comparing Operators
#######################################################

number1 = 11
number2 = 12

print("number1 > number2", number1 > number2) # gt
print("number1 < number2", number1 < number2) # lt
print("number1 >= number2", number1 >= number2) # gte
print("number1 <= number2", number1 <= number2) # lte
print("number1 == number2", number1 == number2)
print("number1 != number2", number1 != number2)


txt1 = "Hello World"
txt2 = "Hello World!"

print(txt1 == txt2)
print(txt1 != txt2)


#######################################################
# Logic Operators
#######################################################

x = 21

# True and True = True
# True and False = False
# False and True = False
# False and False = False


# True or True = True
# True or False = True
# False or True = True
# False or False = False
#
print(5 > x > 0 and x < 10)
print(5 < x < 10)

print(x > 5 or x < 10)

bool_var = not(x > 20 and (x > 5 or x < 10))
print(bool_var)


#######################################################
# Identity Operators
#######################################################

x = 5

print(x is 5)
print(id(x))
print(id(5))

x = 'a'
aa = x * 2
print(id(aa))
print(id('aa'))

print('aa' is not aa)
print('aa' == aa)

x = 5
y = 5

print(id(x))
print(id(y))


#######################################################
# Membership Operators
#######################################################

txt1 = "Hello World"
txt2 = "hello"

print(txt2 in txt1)
print(txt2 not in txt1)


#######################################################
# if/elif/else
#######################################################

number1 = 10
number2 = 20

if number1 < number2:
    print("number1 less than number2")
elif number1 > number2:
    print("number1 greater than number2")
else:
    print("number1 and number2 are equal")

print("after if statement")

if number1 >= number2:
    print("number1 greater than or equal to number2")
else:
    print("number1 less than or equal to number2")


#######################################################
# Ternary Operator
#######################################################

x = 1
zero = "Zero" if x == 0 else "Not Zero"
print(zero)



#######################################################
# Nested Operator
#######################################################

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
operator = input("Enter a operator: ")


if operator == "/":
    if number2 == 0:
        print("Cannot Divide By Zero")
    else:
        print(number1 / number2)
else:
    print("Operator is not /")




