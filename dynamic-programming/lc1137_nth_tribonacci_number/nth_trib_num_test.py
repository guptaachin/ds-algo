import unittest
from nth_trib_num import Solution

class TestSolution(unittest.TestCase):
    def  test_tribonacci(self):
        s = Solution()
        test_cases = [[0, 0],
                      [1, 1],
                      [4, 4]]
        for t in test_cases:
            self.assertEqual(s.tribonacci(t[0]), t[1])

if __name__ == '__main__':
    unittest.main()
