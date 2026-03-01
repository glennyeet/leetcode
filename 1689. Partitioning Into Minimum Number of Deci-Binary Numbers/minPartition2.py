class Solution:
    def minPartitions(self, n: str) -> int:
        # Greedy: O(m) time, where m is the size of n

        min_deci_binary_nums = 0
        for digit in n:
            min_deci_binary_nums = max(min_deci_binary_nums, int(digit))
        return min_deci_binary_nums
