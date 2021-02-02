import unittest
from calc import Calculator
from unittest.mock import patch


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @patch("calc.Calculator.sum",return_value=9)
    def test_sum(self,sum):
        self.assertEqual(sum(2,3), 9)

    def test_sum1(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 6)

    def tearDown(self):
        pass


unittest.main()
