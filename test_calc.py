import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(calc.calc(9.0, 9.0), 'A')

if __name__ == '__main__':
    unittest.main()