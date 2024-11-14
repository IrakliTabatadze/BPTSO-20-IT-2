################################################
# Serialization
################################################
import json

products = {
    'technology': {
        'laptops': {
            '1001': {'brand': 'Apple', 'price': 6000, 'quantity': 2},
            '1002': {'brand': 'HP', 'price': 2000, 'quantity': 10},
        },
        'phones': {
            '2001': {'brand': 'Apple', 'price': 5000, 'quantity': 5},
            '2002': {'brand': 'Samsung', 'price': 3000, 'quantity': 5},
        },
    },
    'clothes': {
        'pants': {
            '3001': {'brand': 'Levi\'s', 'price': 1000, 'quantity': 2},
            '3002': {'brand': 'Lee', 'price': 1000, 'quantity': 2},
        },
        'shirts': {
            '4001': {'brand': 'Adidas', 'price': 5000, 'quantity': 2},
            '4002': {'brand': 'Nike', 'price': 5000, 'quantity': 2},
        }
    }
}

print(products)

json_products = json.dumps(products, indent=4)
print(json_products)


with open('products.json', 'w') as json_file:
    json.dump(products, json_file, indent=4)
    json_file.write(json_products)


from faker import Faker
from random import randint

fake = Faker()

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.score = score
        self.age = age

    def __str__(self):
        return f'{self.name} {self.score} {self.age}'


def custom_serializer(obj: Student):
    if isinstance(obj, Student):
        return {'name': obj.name, 'score': obj.score, 'age': obj.age}
        # return [obj.name, obj.age, obj.score]
    raise TypeError('Cannot serialize object')



student1 = Student(fake.first_name(), randint(20, 50), randint(0, 100))
student2 = Student(fake.first_name(), randint(20, 50), randint(0, 100))
student3 = Student(fake.first_name(), randint(20, 50), randint(0, 100))
student4 = Student(fake.first_name(), randint(20, 50), randint(0, 100))

students_list = [student1, student2, student3, student4]

json_student = json.dumps(students_list, default=custom_serializer)

print(json_student)

with open('students.json', 'w') as json_file:
    json.dump(students_list, json_file, default=custom_serializer, indent=4)


################################################
# Deserialization
################################################


json_products = """{
    "technology": {
        "laptops": {
            "1001": {
                "brand": "Apple",
                "price": 6000,
                "quantity": 2
            },
            "1002": {
                "brand": "HP",
                "price": 2000,
                "quantity": 10
            }
        },
        "phones": {
            "2001": {
                "brand": "Apple",
                "price": 5000,
                "quantity": 5
            },
            "2002": {
                "brand": "Samsung",
                "price": 3000,
                "quantity": 5
            }
        }
    },
    "clothes": {
        "pants": {
            "3001": {
                "brand": "Levi's",
                "price": 1000,
                "quantity": 2
            },
            "3002": {
                "brand": "Lee",
                "price": 1000,
                "quantity": 2
            }
        },
        "shirts": {
            "4001": {
                "brand": "Adidas",
                "price": 5000,
                "quantity": 2
            },
            "4002": {
                "brand": "Nike",
                "price": 5000,
                "quantity": 2
            }
        }
    }
}"""


print(type(json_products))

try:
    products = json.loads(json_products)
except json.decoder.JSONDecodeError as e:
    print(e)

print(products)

with open('products.json', 'r') as json_file:
    try:
        print(json.load(json_file))
    except json.decoder.JSONDecodeError as e:
        print(e)



json_students = """[
    {
        "name": "Christine",
        "score": 71,
        "age": 35
    },
    {
        "name": "Jill",
        "score": 95,
        "age": 46
    },
    {
        "name": "Michael",
        "score": 22,
        "age": 44
    },
    {
        "name": "Jacob",
        "score": 6,
        "age": 39
    }
]"""

class Student:
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.age = age

    def __str__(self):
        return f'{self.name} - {self.score} - {self.age}'


def custom_deserializer(json_data):
    return Student(json_data['name'], json_data['score'], json_data['age'])


students = json.loads(json_students, object_hook=custom_deserializer)
print(students)
for student in students:
    print(student.name)


with open('students.json', 'r') as json_file:
    print(json.load(json_file, object_hook=custom_deserializer))