from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Hash table + Heap: O(nlog(n)) time, O(n) space,
        # where n is the size of nums

        digit_sums = defaultdict(list)
        for num in nums:
            num_copy = num
            digit_sum = 0
            while num_copy != 0:
                digit_sum += num_copy % 10
                num_copy //= 10
            heappush(digit_sums[digit_sum], -num)
        max_sum = -1
        for digit_sum in digit_sums:
            nums = digit_sums[digit_sum]
            if len(digit_sums[digit_sum]) < 2:
                continue
            max_sum = max(max_sum, -heappop(nums) - heappop(nums))
        return max_sum
