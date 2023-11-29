import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part2


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
        self.assertEqual(157, part1(input_list))

    def test_example_part_2(self):
        input_list = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
        self.assertEqual(70, part2(input_list))


if __name__ == '__main__':
    unittest.main()
