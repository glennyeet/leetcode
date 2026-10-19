class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # Sorting: O(n * log(n)) time, O(n) space, where n is the size
        # of nums

        sorted_nums = sorted(nums)
        target_indices = []
        for i, num in enumerate(sorted_nums):
            if num == target:
                target_indices.append(i)
        return target_indices
