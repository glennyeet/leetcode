from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Greedy: O(nlog(n)) time, O(n) space, where n is the size of
        # nums

        sorted_nums = sorted(nums)
        divided_arrays = []
        subarray = []
        for num in sorted_nums:
            subarray.append(num)
            min_num = min(subarray)
            max_num = max(subarray)
            if max_num - min_num > k:
                return []
            if len(subarray) == 3:
                divided_arrays.append(subarray)
                subarray = []
        return divided_arrays
