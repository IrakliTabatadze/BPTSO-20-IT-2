txt = 'Hello World'
print(type(txt))


number = str()
print(number)



class Human:

    nose = 1
    legs = 2
    hands = 2
    ears = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talking(self, message): # ატრიბუტად იღებს ობიექტს
        print(f'{self.name} is saying: {message}')

    @staticmethod
    def walking(): # არ იღებს ატრიბუტად ობიექტს
        print("Walking")

    @classmethod
    def reading(cls): # ატრიბუტად იღებს კლასს
        print("Reading")


human1 = Human('John', 25)
human2 = Human('Anna', 26)

print(human1.legs)
print(human2.legs)

human1.legs = 1

print(human1.legs)
print(human2.legs)

human1.talking('Hello')
human2.talking('Hello')

human1.walking()



###################################################
# Encapsulation
###################################################


class PublicEncapsulation:
    public_cls_attr = 'public_attr'

    def public_method(self):
        print(self.public_cls_attr)


public_obj = PublicEncapsulation()
print(public_obj.public_cls_attr)
public_obj.public_method()




class ProtectedEncapsulation:
    _protected_cls_attr = '_protected_cls_attr'

    def _protected_method(self):
        print('Protected')

protected_obj = ProtectedEncapsulation()
protected_obj._protected_method()
print(protected_obj._protected_cls_attr)


class PrivateEncapsulation:
    __private_cls_attr = '__private_cls_attr'

    def __private_method(self):
        print(self.__private_cls_attr)

    def public_method(self):
        self.__private_method()


private_obj = PrivateEncapsulation()
print(private_obj.__private_cls_attr)
private_obj.__private_method()
private_obj.public_method()



###################################################
# Inheritance
###################################################


class Animal:
    legs = 4

    def __init__(self, name):
        self.name = name

    def running(self):
        print(f'{self.name} can run')


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def meow(self):
        print(f"{self.name} can Meow")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} can Bark")

cat = Cat('Garfield', 'Orange')
print(cat.legs)

dog = Dog('Fluffy', 'Breed')
print(dog.legs)

cat.running()
dog.running()


###################################################
# Multiple Inheritance
###################################################


class Mother:
    def __init__(self, name, eye_color):
        self.name = name
        self.eye_color = eye_color

    def bake_cookies(self):
        print(f"{self.name} can bake best cookies in the world")

class Father:
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color

    def tell_jokes(self):
        print(f'{self.name} can tell funny jokes')


class Child(Mother, Father):
    def __init__(self, name, hair_color, eye_color, profession):
        Mother.__init__(self, name, eye_color)
        Father.__init__(self, name, hair_color)
        self.profession = profession

    def coding(self):
        print(f'{self.name} can code')

child = Child('John', 'Black', 'Blue', 'Developer')
child.coding()
child.tell_jokes()
child.bake_cookies()


###################################################
# Polymorphism
###################################################

class Shape:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def area(self):
        print('You need to rewrite this method in child class')


class Rectangle(Shape):
    def area(self):
        width, height = self.dimensions
        return width * height

class Circle(Shape):
    def area(self):
        return 3.14 * self.dimensions ** 2


rect = Rectangle([10, 20])
circle = Circle(10)

print(rect.area())
print(circle.area())