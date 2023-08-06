from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            temp = abs(num)
            nums[temp-1] = -abs(nums[temp-1])
        result = []
        length = len(nums)
        for i in range(length):
            if nums[i] > 0:
                result.append(i+1)
        return result