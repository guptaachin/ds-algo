import unittest
from lc_2997 import Solution

class TestSolution(unittest.TestCase):
    def test_minOperations(self):
        s = Solution()
        self.assertEqual(s.minOperations([2,1,3,4], 1), 2)

if __name__ == "__main__":
    unittest.main()