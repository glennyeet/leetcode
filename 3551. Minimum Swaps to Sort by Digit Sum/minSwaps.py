from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Math + Hash Table + Sorting: O(n * log(n)) time,
        # O(n) space

        n = len(nums)

        def find_digit_sum(num: int) -> int:
            cur_num = num
            digit_sum = 0
            while cur_num:
                digit_sum += cur_num % 10
                cur_num //= 10
            return digit_sum

        nums_index = {}
        digit_sums = []
        for i, num in enumerate(nums):
            nums_index[num] = i
            digit_sums.append((find_digit_sum(num), num))
        digit_sums.sort()
        nums_sorted_index = {}
        for i, (_, num) in enumerate(digit_sums):
            nums_sorted_index[nums_index[num]] = i
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = nums_sorted_index[j]
        min_swaps = n - cycles
        return min_swaps
