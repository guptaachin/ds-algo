from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = []
        for i in range(0, len(sorted_nums), 3):
            lb = i
            rb = i + 3
            bounds = (sorted_nums[i]-k, sorted_nums[i]+k)
            if bounds[0] <= sorted_nums[rb-1] <= bounds[1]:
                ans.append(sorted_nums[lb:rb])
            else:
                return []
        return ans
        