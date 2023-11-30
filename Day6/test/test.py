import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''
        self.assertEqual(7, part1(input_list))

        input_list = '''bvwbjplbgvbhsrlpgdmjqwftvncz'''
        self.assertEqual(5, part1(input_list))

        input_list = '''nppdvjthqldpwncqszvftbrmjlhg'''
        self.assertEqual(6, part1(input_list))

        input_list = '''nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'''
        self.assertEqual(10, part1(input_list))

        input_list = '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''
        self.assertEqual(11, part1(input_list))

    def test_example_part_2(self):
        input_list = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''
        self.assertEqual(19, part2(input_list))

        input_list = '''bvwbjplbgvbhsrlpgdmjqwftvncz'''
        self.assertEqual(23, part2(input_list))

        input_list = '''nppdvjthqldpwncqszvftbrmjlhg'''
        self.assertEqual(23, part2(input_list))

        input_list = '''nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'''
        self.assertEqual(29, part2(input_list))

        input_list = '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''
        self.assertEqual(26, part2(input_list))


if __name__ == '__main__':
    unittest.main()
