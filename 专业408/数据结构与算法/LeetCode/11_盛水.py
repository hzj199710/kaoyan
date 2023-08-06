class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            if height[left] < height[right]:
                new_area = (right -left) * height[left]
                area = max(area, new_area)
                new_left = -1
                for i in range(left, right):
                    if height[i] > height[left]:
                        new_left = i
                        break
                if new_left > 0:
                    left = new_left
                else:
                    break
            else:
                new_area = (right -left) * height[right]
                area = max(area, new_area)
                new_right = -1
                for i in range(right, left, -1):
                    if height[i] > height[right]:
                        new_right = i
                        break
                if new_right > 0:
                    right = new_right
                else:
                    break
        return area