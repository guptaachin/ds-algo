from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            max_ = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_ = max(max_, dp[j])
            dp[i] = max_ + 1
        return max(dp)
