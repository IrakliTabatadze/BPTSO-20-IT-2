
print("a" > "A")

txt = 'Hello World!!!'

print(txt.upper())
print(txt.lower())

txt = txt.upper()
print(txt)

length = len(txt)
print(length)




######################################################


hello = 'Hello'
world = ' World'

print(hello + world)

result = ''

while True:
    number = int(input('Enter a number: '))

    if number > 0:
        result += "User entered positive number \n"

    if number == 0:
        break

print(result)


print("Hello World" * 5)


txt = "Hello World!!!"
print(txt[6])
print(txt[len(txt) - 1])
print(txt[-6])
print(txt[1:8])
print(txt[-5:-1])
print(txt[5:])
print(txt[:7])




##############################################
# String Methods
##############################################

print("Hello World")

txt = "Hello World"
txt.upper()

number = 10


first_name = 'john'.capitalize()
last_name = 'doe'.capitalize()

print(first_name + " " + last_name)


txt = 'Hello Hello. Hello hello'

print(txt.count('Hello'))
print(txt.index('H'))

txt_split = txt.split()
print(txt_split)


txt = ' Hello World '

print(txt.strip())

txt = '''  Hello\n\n\n\n\t\tWorld   '''
txt = txt.replace('\n', '').replace('\t', ' ')

print(txt.strip())


##############################################
# String Formatting
##############################################

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

result = '%d + %d = %d' % (number1, number2, number1 + number2)
print(result)

result = '{} + {} = {}'.format(number1, number2, number1 + number2)
result = '{2} + {0} = {1}'.format(number1, number2, number1 + number2)

result = '{number1} + {number2} = {addition}'
print(result.format(number1=number1, number2=number2, addition=number1+number2))

url = 'www.google.com/{search_word}'

url.format(search_word='python')
url.format(search_word='java')
url.format(search_word='c#')


result = f'{number1} + {number2} = {number1 + number2}'
result = F'{number1} + {number2} = {number1 + number2}'
print(result)
