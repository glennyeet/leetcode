class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_len = 0
        local_max_len = 0
        for num in nums:
            if num == max_num:
                local_max_len += 1
            else:
                max_len = max(max_len, local_max_len)
                local_max_len = 0
        max_len = max(max_len, local_max_len)
        return max_len
