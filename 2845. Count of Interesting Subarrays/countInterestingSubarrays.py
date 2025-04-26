from typing import List
from collections import Counter


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Prefix Sum + Hash Table: O(n) time, O(n) space, where n is the size of nums

        cnts = [0]
        for num in nums:
            cnts.append(cnts[-1] + (num % modulo == k))
        interesting_subarrays = 0
        cnt_modulo_counter = Counter()
        for cnt in cnts:
            interesting_subarrays += cnt_modulo_counter[(cnt - k) % modulo]
            cnt_modulo_counter[cnt % modulo] += 1
        return interesting_subarrays
