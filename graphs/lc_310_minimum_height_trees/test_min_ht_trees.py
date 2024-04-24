import unittest
from min_ht_trees import Solution

class TestSolution(unittest.TestCase):
    def test_findMinHeightTrees(self):
        test_cases = [
            [4, [[1,0],[1,2],[1,3]], [1]], 
            [6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3,4]]
        ]
        s = Solution()
        for t in test_cases:
            self.assertEqual(t[2], s.findMinHeightTrees(t[0], t[1]))

if __name__ == "__main__":
    unittest.main()