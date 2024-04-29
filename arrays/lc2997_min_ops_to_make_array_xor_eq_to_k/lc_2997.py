from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # find xor of all elements
        e_xor = 0
        for n in nums:
            e_xor ^= n
        # xor with k to find deviations
        ans = e_xor ^ k
        # count deviations
        res = 0
        while ans != 0:
            if ans & 1 == 1:
                res += 1
            ans = ans >> 1
        return res