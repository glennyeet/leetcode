from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # Prefix Sum: O(n * c) time, O(n) space, where c is the size of
        # conflictingPairs

        b_to_a_mapping = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            b_to_a_mapping[b].append(a)
        max_a = [0, 0]
        no_removal_subarrays = 0
        one_removal_subarrays = [0] * (n + 1)
        for i in range(1, n + 1):
            for a in b_to_a_mapping[i]:
                max_a = max(max_a, [a, max_a[0]], [max_a[0], a])
            no_removal_subarrays += i - max_a[0]
            one_removal_subarrays[max_a[0]] += max_a[0] - max_a[1]
        return no_removal_subarrays + max(one_removal_subarrays)
