import unittest
import logics


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(logics.add(10, 15), 25)
        self.assertEqual(logics.add(0, 15), 15)
        self.assertEqual(logics.add(-10, 15), 5)
        self.assertEqual(logics.add(-10, -15), -25)
        self.assertEqual(logics.add(0, -15), -15)

    def test_divide(self):
        self.assertEqual(logics.divide(10, 5), 2)

        with self.assertRaises(ValueError) as context:
            logics.divide(10, 0)

        self.assertEqual(str(context.exception), 'Cannot divide by zero')


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('SetUp')
        self.employee1 = logics.Employee('John', 'Doe', 2000)

    def tearDown(self):
        print('TearDown')

    def test_email(self):
        print('Test Email')
        self.assertEqual(self.employee1.email, 'John.Doe@gmail.com')

        self.employee1.first_name = 'Kate'

        self.assertEqual(self.employee1.email, 'Kate.Doe@gmail.com')

        self.employee1.salary = 10000

    def test_apply_raise(self):
        print('Test Apply Raise')
        self.employee1.apply_raise()

        self.assertEqual(self.employee1.salary, 4000)

        self.employee1.apply_raise()

        self.assertEqual(self.employee1.salary, 8000)


if __name__ == '__main__':
    unittest.main()
