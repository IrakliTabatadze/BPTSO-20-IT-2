#################################################
# Property, Getter, Setter, Deleter
#################################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('John', 25)

print(person1.name)
print(person1.age)

person1.name = 'Anna'
person1.age = 26

print(person1.name)
print(person1.age)

del person1.name
del person1.age

print(person1.age)
print(person1.name)


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @name.getter
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age


person1 = Person("John", 25)

print(person1.name)
print(person1.age)

person1.name = "Anna"
person1.age = 26
print(person1.name)
print(person1.age)

del person1.age
del person1.name

print(person1.age)
print(person1.name)


#################################################
# Abstract Classes
#################################################

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



circle = Circle(10)
print(circle.area())

rect = Rectangle(10,15)


#################################################
# Method Overload
#################################################

class Calculator:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


calc = Calculator()
print(calc.add(10, 15))


class Calculator:
    def add(self, x, y):
        if isinstance(x, (float, int)) and isinstance(y, (float, int)):
            result = x + y
            return f'sum of two numbers is : {result}'
        elif isinstance(x, str) and isinstance(y, str):
            result = x + y
            return f'concatenation of two strings is : {result}'

calc = Calculator()
print(calc.add(10, 15))
print(calc.add('Hello', 'World'))


from multipledispatch import dispatch

class Calculator:

    @staticmethod
    @dispatch(int, int)
    def add(x, y):
        result = x + y
        return f'sum of two numbers is : {result}'

    @staticmethod
    @dispatch(int, int, int)
    def add(x, y, z):
        result = x + y + z
        return f'sum of three numbers is : {result}'

    @staticmethod
    @dispatch(str, str)
    def add(a, b):
        result = a + b
        return f'concatenation of two strings is : {result}'

calc = Calculator()
print(calc.add(10, 15))
print(calc.add(10, 15, 20))
print(calc.add('Hello', 'World'))


################################################
Magic Methods
################################################

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Please provide two vectors')
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y


vector1 = Vector(1, 2)
vector2 = Vector(1, 2)
vector3 = vector1 + vector2
print(f'Vector({vector3.x}, {vector3.y})')
print(vector1 == vector2)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name} is {self.age} years old'

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.age})'


person1 = Person("John", "Doe", 25)
print(person1)

print({1, 2, 3, 4})
print(frozenset({1, 2, 3, 4}))
