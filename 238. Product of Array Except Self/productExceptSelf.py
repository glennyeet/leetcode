from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix Sum: O(n) time, O(n) space

        n = len(nums)
        prefix_products = [1]
        for num in nums:
            prefix_products.append(prefix_products[-1] * num)
        suffix_products = [1]
        for num in reversed(nums):
            suffix_products.append(suffix_products[-1] * num)
        suffix_products.reverse()
        non_self_products = [0] * n
        for i in range(n):
            non_self_products[i] = prefix_products[i] * suffix_products[i + 1]
        return non_self_products
