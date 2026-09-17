from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # Sliding Window: O(n) time, O(n) space

        n = len(arr)
        min_len_ending_at = [float("inf")] * n
        cur_sum = 0
        min_len_before_l = float("inf")
        min_len = float("inf")
        l = 0
        r = 0
        while r < n:
            cur_sum += arr[r]
            r += 1
            while cur_sum > target:
                cur_sum -= arr[l]
                min_len_before_l = min(min_len_before_l, min_len_ending_at[l])
                l += 1
            if cur_sum == target:
                min_len_ending_at[r - 1] = min(min_len_ending_at[r - 1], r - l)
                min_len = min(min_len, min_len_before_l + r - l)
        if min_len == float("inf"):
            return -1
        return min_len
