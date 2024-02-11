class Solution:
    def climbStairs(self, n: int) -> int:
        # This is a 1D DP
        # Think about the ways to reach the top from stairs t-1 ans t-2

        # Think the problem in reverse back from Top
        # Then you realize you can just code it inverse
        s_1 = 1
        if n == 1: return s_1
        s_2 = 2
        if n == 2: return s_2
        s = s_1 + s_2
        # Build number of ways needed
        for _ in range(n-2):
            s = s_1 + s_2
            s_1 = s_2
            s_2 = s
        return s
