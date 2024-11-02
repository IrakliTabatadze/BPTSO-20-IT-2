########################################
# Decorators
########################################

def decorator(func):
    def wrapper(*args, **kwargs):
        #print(args)
        #return func(*args, **kwargs)
        #x = args[0] + 100
        #y = args[1] + 100
        #return func(x, y)
        x = args[0]
        y = args[1]

        if isinstance(x, (float, int)) and isinstance(y, (float, int)):
            return func(x, y)
        else:
            raise TypeError('Argument must be float or int')

    return wrapper


@decorator
def calculate(x, y):
    return f'The sum of {x} and {y}: {x*y}'

print(calculate(10, '20'))


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper
    return decorator



@repeat(3)
def print_hello(name='John'):
    print(f"Hello {name}")

print_hello()


########################################
# Functors
########################################

class Functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(name)
        print(args)
        lst = [self.func(item) for item in args]
        return lst


def square(x):
    return x ** 2

functor = Functor(square)
print(functor(10, 20, 30, 40))


########################################
# Descriptors
########################################

class Descriptor:
    def __get__(self, instance, owner):
        print(f'Getting value of name: {instance.__dict__}')
        return instance.name

    def __set__(self, instance, value):
        print(f'Setting value of name: {value}')
        instance.name = value

    def __delete__(self, instance):
        print(f'Deleting value of name: {instance.name}')
        del instance.name

class Person:

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.birthday = '2024'

    descriptor = Descriptor()

person1 = Person('John')
print(person1.descriptor)
person1.descriptor = 'Kate'
print(person1.descriptor)
del person1.descriptor
print(person1.descriptor)


########################################
# MetaClass
########################################


class Car(type):
    def __new__(cls, name, bases, dct):
        print(bases)
        instance = super().__new__(cls, name, bases, dct)
        return instance

    def print_something(cls):
        print(cls.__name__)

# print(type(Car))

class ElectricCar(metaclass=Car):
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        return self.brand

el_car = ElectricCar('Tesla')
print(el_car.show_info())
print(type(ElectricCar))