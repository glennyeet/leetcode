from collections import Counter


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Hash table: O(n) time, O(n) space

        n = len(nums)
        differences_counter = Counter()
        for i, num in enumerate(nums):
            differences_counter[num - i] += 1
        good_pairs = 0
        for count in differences_counter.values():
            good_pairs += count * (count - 1) // 2
        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs
