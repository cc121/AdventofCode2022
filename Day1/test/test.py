import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from MostCalories import get_most_calories, get_top_three_calories


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        calorie_list = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
        self.assertEqual(24000, get_most_calories(calorie_list))


    def test_example_part_2(self):
        calorie_list = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
        self.assertEqual(45000, get_top_three_calories(calorie_list))


if __name__ == '__main__':
    unittest.main()
