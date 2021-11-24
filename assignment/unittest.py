from calculator import Calculator
import unittest

class CalculatorTests(unittest.TestCase):
    def add(self):
        calc=Calculator()
        self.assertEqual(6,calc.add(1,5))

if __name__=='__main__':
    unittest.main()