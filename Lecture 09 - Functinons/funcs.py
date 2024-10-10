import math

def circle_area(pi):
    def whole_area(radius):
        return pi * radius ** 2

    return whole_area


func = circle_area(math.pi)
# print(circle_area)
print(func(10))
print(func(20))
print(func(30))




# LEGB - Local, Enclosed, Global


x = 10 # Global Variable

def legb():
    # global x
    # x = x + 1
    x = 25 # Enclosed Variable
    print(x)
    def nested_func():
        # global x
        x = 50 # Local Variable
        print(x)

    nested_func()

legb()





###############################################
# Recursive Functions
###############################################


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))

def test():
    test()

test()

