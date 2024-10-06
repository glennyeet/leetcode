class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0
        min_len = n
        prefix_remainder_to_index = {}  # from index 0 to left - 1
        prefix_remainder_to_index[0] = -1
        prefix_remainder = 0
        for right in range(n):
            prefix_remainder = (prefix_remainder + nums[right]) % p
            target = (prefix_remainder - remainder) % p
            if target in prefix_remainder_to_index:
                left = prefix_remainder_to_index[target] + 1
                min_len = min(min_len, right - left + 1)
            prefix_remainder_to_index[prefix_remainder] = right
        if min_len == n:
            return -1
        return min_len
