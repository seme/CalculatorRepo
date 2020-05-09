import calculator


class TestCalculator:

    def test_multiply(self):
        assert 200 == calculator.multiply(5, 40)
