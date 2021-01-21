import unittest
from calculator import Calculator

calc = Calculator()

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.exec('{"+": [1, 2]}'), 2 + 1)
        self.assertEqual(calc.exec('{"+": [1, -2]}'), 1 + -2)
        self.assertEqual(calc.exec('{"+": [-1, 2]}'), -1 + 2) 
        self.assertEqual(calc.exec('{"+": [-1, -4]}'), -1 + -4)

    def test_sub(self):
        self.assertEqual(calc.exec('{"-": [1, 2]}'), 1 - 2)
        self.assertEqual(calc.exec('{"-": [1, -2]}'), 1 - - 2)
        self.assertEqual(calc.exec('{"-": [-1, 2]}'), -1 - 2) 
        self.assertEqual(calc.exec('{"-": [-1, -4]}'), -1 - -4)     

    def test_mul(self):
        self.assertEqual(calc.exec('{"*": [3, 2]}'), 3 * 2)
        self.assertEqual(calc.exec('{"*": [-3, 2]}'), -3 * 2 )
        self.assertEqual(calc.exec('{"*": [3, -2]}'), 3 * -2 )
        self.assertEqual(calc.exec('{"*": [-3, -2]}'), -3 * -2)

    def test_div(self):
        self.assertEqual(calc.exec('{"/": [3, 2]}'), 3 / 2)
        self.assertEqual(calc.exec('{"/": [-3, 2]}'), -3 / 2)
        self.assertEqual(calc.exec('{"/": [3, -2]}'), 3 / -2)
        self.assertEqual(calc.exec('{"/": [-3, -2]}'), -3 / -2)

    def test_compound_expressions(self):
        self.assertEqual(calc.exec('{"+": [2, {"*":[2, 2]}]}'), 2 + 2 * 2)
        self.assertEqual(calc.exec('{"*": [3, {"+":[2, 2]}]}'), 3 * (2 + 2))
        self.assertEqual(calc.exec('{"/": [{"*": [3, 2]}, {"*": [3, 4]}]}'), (3 * 2) / (3 * 4))
if __name__ == '__main__':
    unittest.main()