import pytest
from app.calculator import Calculator


class TestsCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multyply_success(self):
        assert self.calculator.multiply(self, 5, 6) == 30, 'Ошибка в умножении'

    def test_adding_success(self):
        assert self.calculator.adding(self, 12, 21) == 33, 'Ошибка в сложении'

    def test_division_success(self):
        assert self.calculator.division(self, 12, 4) == 3, 'Ошибка в делении'

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 24, 4) == 20, 'Ошибка в вычитании'

    def test_adding_unsuccess(self):
        assert self.calculator.adding(self, 2, 2) != 5, 'Ошибка негативного теста на сложение'

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError) as e:
            assert self.calculator.division(self, 12, 0), 'Ошибка при делении на ноль'

    def teardown(self):
        print('End of test')
