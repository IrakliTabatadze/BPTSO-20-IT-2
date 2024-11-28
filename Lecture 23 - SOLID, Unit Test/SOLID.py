# S O L I D

# S - Single Responsibility Principle

class TextFileManager:

    def write_txt(self):
        pass

    def read_txt(self):
        pass


class ZipFileManager:
    def compress(self):
        pass

    def decompress(self):
        pass


# O - Open Closed Principle

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

    def draw(self):
        pass


# L - Liskov Substitution Principle

class KitchenApp:
    def on(self):
        pass

    def off(self):
        pass


class Juicer(KitchenApp):
    def on(self):
        pass

    def off(self):
        pass

    def juice(self):
        pass


class KitchenAppWithTemperature(KitchenApp):
    def set_temperature(self):
        pass


class Toster(KitchenAppWithTemperature):
    def on(self):
        pass

    def off(self):
        pass

    def set_temperature(self):
        pass

    def toasting(self):
        pass


# I - Interface Segregation Principle

class Printer:
    def printing(self):
        pass


class Scanner:
    def scanning(self):
        pass


class Xerox:
    def xerox(self):
        pass


class Fax:
    def fax(self):
        pass


class PrintingDevice(Printer):
    pass


class ScanningDevice(Scanner):
    pass


class MultifunctionalDevice(Printer, Scanner):
    pass


# D - Dependency Inversion Principle

# class Logger:
#     def log(self, message):
#         with open('txt.txt', 'w') as file:
#             pass
#
#
# class Calculator:
#     def __init__(self):
#         self.logger = Logger()
#
#     def plus(self, number1, number2):
#         result = number1 + number2
#
#         self.logger.log(f'{number1} + {number2} = {result}')
#         return result


from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    @abstractmethod
    def log(self):
        pass


class Logger(LoggerInterface):
    def log(self, message):
        with open('txt.txt', 'w') as file:
            pass


class Calculator:
    def __init__(self, logger):
        self.logger = logger

    def plus(self, num1, num2):
        result = num1 + num2

        self.logger.log(f'{num1} + {num2} = {result}')
        return result


calculator = Calculator(Logger())
