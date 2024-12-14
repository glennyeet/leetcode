class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        continuous_subarrays = 0
        l = 0
        min_num = nums[0]
        max_num = nums[0]
        for r, num in enumerate(nums):
            min_num = min(min_num, num)
            max_num = max(max_num, num)
            if max_num - min_num <= 2:
                continue
            window = r - l
            continuous_subarrays += window * (window + 1) // 2
            l = r
            min_num = num
            max_num = num
            while abs(nums[l - 1] - num) <= 2:
                l -= 1
                min_num = min(min_num, nums[l])
                max_num = max(max_num, nums[l])
            overlap = r - l
            continuous_subarrays -= overlap * (overlap + 1) // 2
        else:
            window = r + 1 - l
            continuous_subarrays += window * (window + 1) // 2
        return continuous_subarrays
