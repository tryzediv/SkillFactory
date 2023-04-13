import pytest
from calculator import Calculator
import random

x = random.randint(0, 255)
y = random.randint(0, 255)


class TestsCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multyply_success(self):
        assert self.calculator.multiply(self, x, y) == x * y

    def test_adding_success(self):
        assert self.calculator.adding(self, x, y) == x + y

    def test_adding_unsuccess(self):
        assert self.calculator.adding(self, 2, 2) != 5

    def test_zero_division(self):
        if y == 0:
            with pytest.raises(ZeroDivisionError) as e:
                assert self.calculator.division(self, x, y)
        else:
            assert self.calculator.division(self, x, y) == x / y
    def teardown(self):
        print('End of test')
