
# 2

number1 = int(input('Please Input a number'))
number2 = int(input('Please Input a number'))
operator = input('Please Input Math Operator')

operators_dict = {
    '+': number1 + number2,
    '-': number1 - number2,
    '*': number1 * number2,
    '/': number1 / number2
}

print(operators_dict.get(operator, 'Please Enter Operators (+, -, *, /)'))



# 3

lst = [x for x in range(1, 11)]
dct = {f'{x}': x**2 for x in range(1, 11)}
print(dct)


# 4

departments = {
    'IT': [
        {'first_name': 'John', 'last_name': 'Doe', 'salary': 3000},
        {'first_name': 'Jane', 'last_name': 'Doe', 'salary': 4000},
    ],
    'HR': [
        {'first_name': 'John', 'last_name': 'Doe', 'salary': 2000},
        {'first_name': 'Jane', 'last_name': 'Doe', 'salary': 3000},
    ],
    'Marketing': [
        {'first_name': 'John', 'last_name': 'Doe', 'salary': 5000},
        {'first_name': 'Jane', 'last_name': 'Doe', 'salary': 10000},
    ]
}


average_salaries = {}

for department, employees in departments.items():
    total_salary = sum(employee['salary'] for employee in employees)
    employees_count = len(employees)
    average_salary = total_salary / employees_count
    average_salaries[department] = average_salary

print(average_salaries)