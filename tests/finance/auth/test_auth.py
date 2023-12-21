import unittest
from finance.routs.auth.demo import Demo


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.demo = Demo()

    def test_test_method_with_positive_numbers(self):
        # Проверка метода с положительными числами
        result = self.demo.test_method(3, 5)
        self.assertEqual(result, 8)

    def test_test_method_with_negative_numbers(self):
        # Проверка метода с отрицательными числами
        result = self.demo.test_method(-3, -5)
        self.assertEqual(result, -8)

    def test_test_method_with_mixed_numbers(self):
        # Проверка метода с смешанными числами
        result = self.demo.test_method(-3, 5)
        self.assertEqual(result, 2)

    def test_test_method_with_zero(self):
        # Проверка метода с нулевыми числами
        result = self.demo.test_method(0, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()