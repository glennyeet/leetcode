from collections import Counter


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Hash map: O(n^2) time, O(n^2) space

        n = len(nums)
        product_counter = Counter()
        for i in range(n):
            for j in range(i + 1, n):
                product_counter[nums[i] * nums[j]] += 1
        tuples = 0
        for count in product_counter.values():
            tuples += 8 * (count * (count - 1) // 2)
        return tuples
