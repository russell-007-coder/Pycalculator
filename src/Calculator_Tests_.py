import unittest
from Calculator_ import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator_()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add(self):
        test_data = CsvReader("src/UnitTest Addition.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sub(self):
            test_data = CsvReader("src/UnitTest Subtraction.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multi(self):
            test_data = CsvReader("src/UnitTest Multiplication.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

    def test_div(self):
            test_data = CsvReader("src/UnitTest_Division.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
                self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square(self):
            test_data = CsvReader("src/UnitTest Square.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.squares(row['Value 1']), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrroot(self):
            test_data = CsvReader("src/UnitTest SquareRoot.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.square_root(row['Value 1']), round(float(row['Result']), 7))
                self.assertEqual(self.calculator.result, round(float(row['Result']), 7))



if __name__ == '__main__':
    unittest.main()