import unittest
from one import count_ways_to_climb


class TestCountWaysToClimb(unittest.TestCase):
    def test_count_ways_to_climb(self):
        self.assertEqual(count_ways_to_climb(8), 34)
        self.assertEqual(count_ways_to_climb(5), 8)


if __name__ == '__main__':
    unittest.main()