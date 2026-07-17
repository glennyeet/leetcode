from bisect import bisect_left
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Inclusion-Exclusion Principle + Prefix Sum + Binary Search:
        # O(m * log(m) + q * log(m)) time, O(m) space, where m is the max
        # number in nums and q is the size of queries

        max_num = max(nums)
        counter = [0] * (max_num + 1)
        for num in nums:
            counter[num] += 1
        for i in range(1, max_num + 1):
            for j in range(i * 2, max_num + 1, i):
                counter[i] += counter[j]
        for i in range(1, max_num + 1):
            counter[i] = counter[i] * (counter[i] - 1) // 2
        for i in reversed(range(1, max_num + 1)):
            for j in range(i * 2, max_num + 1, i):
                counter[i] -= counter[j]
        for i in range(1, max_num + 1):
            counter[i] += counter[i - 1]
        answer = []
        for query in queries:
            gcd_pairs = bisect_left(counter, query + 1)
            answer.append(gcd_pairs)
        return answer
