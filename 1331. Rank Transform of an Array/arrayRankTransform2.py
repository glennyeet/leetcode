from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Hash Table + Sorting: O(n * log(n)) time, O(n) space,
        # where n is the size of arr

        sorted_arr = sorted(set(arr))
        num_to_rank = {}
        for i, num in enumerate(sorted_arr):
            num_to_rank[num] = i + 1
        arr_ranks = []
        for num in arr:
            arr_ranks.append(num_to_rank[num])
        return arr_ranks
