import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 4, 4) == 16

    def test_division_calculate_correctly(self):
        assert  self.calc.division(self, 15, 5) == 3

    def test_subtraction_calculate_correctly(self):
        assert  self.calc.subtraction(self, 13, 6) == 7

    def test_adding_calculate_correctly(self):
        assert  self.calc.adding(self, 10, 11) == 21