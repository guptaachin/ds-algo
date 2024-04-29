import unittest
from lc_2997 import Solution

class TestSolution(unittest.TestCase):
    def test_minOperations(self):
        s = Solution()
        assert 2 == s.minOperations([2,1,3,4], 1)

if __name__ == "__main__":
    unittest.main()