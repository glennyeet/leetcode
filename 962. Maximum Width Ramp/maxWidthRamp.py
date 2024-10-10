class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Two Pointers
        n = len(nums)
        max_right_num = [0] * n
        prev_max_num = 0
        i = n - 1
        for num in reversed(nums):
            max_right_num[i] = max(prev_max_num, num)
            prev_max_num = max_right_num[i]
            i -= 1
        i = 0
        max_width = 0
        for j, _ in enumerate(nums):
            while nums[i] > max_right_num[j]:
                i += 1
            max_width = max(max_width, j - i)
        return max_width
