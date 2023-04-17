import pytest
from app.calculator import Calculator


class TestsCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multyply_success(self):
        assert self.calculator.multiply(self, 5, 6) == 30, ''

    def test_adding_success(self):
        assert self.calculator.adding(self, 12, 21) == 33, ''

    def test_division_success(self):
        assert self.calculator.division(self, 12, 4) == 3, ''

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 24, 4) == 20, ''

    def test_adding_unsuccess(self):
        assert self.calculator.adding(self, 2, 2) != 5, ''

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError) as e:
            assert self.calculator.division(self, 12, 0), ''

    def teardown(self):
        print('End of test')
