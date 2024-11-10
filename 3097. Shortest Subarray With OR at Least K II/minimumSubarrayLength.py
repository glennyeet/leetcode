from math import inf, isinf


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits_count = [0] * 32
        or_sum = 0

        def update_or_sum(num: int, diff: int) -> int:
            for i in range(len(bits_count)):
                if num & 1 << i:
                    bits_count[i] += diff
            new_sum = 0
            for i in range(len(bits_count)):
                if bits_count[i]:
                    new_sum |= 1 << i
            return new_sum

        special_len = inf
        l = 0
        for r, num in enumerate(nums):
            or_sum = update_or_sum(num, 1)
            while or_sum >= k and l <= r:
                special_len = min(special_len, r - l + 1)
                or_sum = update_or_sum(nums[l], -1)
                l += 1
        if isinf(special_len):
            return -1
        return special_len
