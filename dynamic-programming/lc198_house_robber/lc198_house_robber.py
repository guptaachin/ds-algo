from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2] + nums[0]
        for h in range(3, len(nums)):
            dp[h] = nums[h] + max(dp[h-2], dp[h-3])

        return max(dp)
