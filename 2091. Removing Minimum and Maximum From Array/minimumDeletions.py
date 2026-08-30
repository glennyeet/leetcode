from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # Greedy: O(n * log(n)) time, O(1) space

        n = len(nums)
        min_num_index = nums.index(min(nums))
        max_num_index = nums.index(max(nums))
        if min_num_index <= max_num_index:
            first_index = min_num_index
            second_index = max_num_index
        else:
            first_index = max_num_index
            second_index = min_num_index
        distances = sorted(
            [first_index + 1, second_index - first_index, n - second_index]
        )
        min_deletions = distances[0] + distances[1]
        return min_deletions
