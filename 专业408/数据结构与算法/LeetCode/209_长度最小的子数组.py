class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = len(nums) + 1
        sum = 0
        for right, x in enumerate(nums):
            sum += x
            while sum - nums[left] >= target:
                sum = sum - nums[left]
                left += 1
            if sum >= target:
                ans = min(ans, right - left + 1)
        return ans if ans < len(nums) + 1 else 0