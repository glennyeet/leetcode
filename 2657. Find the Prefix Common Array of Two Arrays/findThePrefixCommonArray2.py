from typing import List
from collections import Counter


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Hash Table: O(n) time, O(n) space

        n = len(A)
        prefix_common_array = [0] * n
        A_counter = Counter()
        B_counter = Counter()
        common_nums = set()
        for i, (num1, num2) in enumerate(zip(A, B)):
            A_counter[num1] += 1
            B_counter[num2] += 1
            if A_counter[num1] and B_counter[num1]:
                common_nums.add(num1)
            if A_counter[num2] and B_counter[num2]:
                common_nums.add(num2)
            prefix_common_array[i] = len(common_nums)
        return prefix_common_array
