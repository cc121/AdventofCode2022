import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from RockPaperScissors import calculate_score, calculate_hand_and_score


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''A Y
B X
C Z'''
        self.assertEqual(15, calculate_score(input_list))

    def test_example_part_2(self):
        input_list = '''A Y
B X
C Z'''
        self.assertEqual(12, calculate_hand_and_score(input_list))


if __name__ == '__main__':
    unittest.main()
