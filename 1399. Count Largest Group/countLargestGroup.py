from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        # Hash Table: O(nlog(n)) time, O(n) space

        digit_sums_counter = Counter()
        max_size = 0
        for i in range(1, n + 1):
            digit_sum = 0
            for digit in str(i):
                digit_sum += int(digit)
            digit_sums_counter[digit_sum] += 1
            max_size = max(max_size, digit_sums_counter[digit_sum])
        max_size_groups = 0
        for group in digit_sums_counter:
            max_size_groups += digit_sums_counter[group] == max_size
        return max_size_groups
