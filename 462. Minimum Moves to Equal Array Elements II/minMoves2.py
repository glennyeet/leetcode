class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Math: O(n * log(n)) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        if n % 2 == 0:
            medians = [sorted_nums[n // 2]]
        else:
            medians = [sorted_nums[n // 2 - 1], sorted_nums[n // 2]]
        min_moves = float("inf")
        for median in medians:
            moves = 0
            for num in sorted_nums:
                moves += abs(num - median)
            min_moves = min(min_moves, moves)
        return min_moves
