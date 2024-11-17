from collections import deque
from math import inf


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prev_sums = deque()
        cur_sum = 0
        min_len = inf
        for r, num in enumerate(nums):
            cur_sum += num
            if cur_sum >= k:
                min_len = min(min_len, r + 1)
            while prev_sums and cur_sum - prev_sums[0][0] >= k:
                _, l = prev_sums.popleft()
                min_len = min(min_len, r - l)
            while prev_sums and prev_sums[-1][0] >= cur_sum:
                prev_sums.pop()
            prev_sums.append((cur_sum, r))
        if min_len == inf:
            return -1
        return min_len
