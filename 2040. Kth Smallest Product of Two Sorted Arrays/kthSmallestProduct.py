from typing import List
from bisect import bisect_left, bisect_right
from math import ceil


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Binary Search: O(r * mlog(n))) time, O(1) space, where r is the range
        # of possible products and m is the size of nums1

        n = len(nums2)

        def count_products_leq_target(target: int) -> int:
            count = 0
            for num in nums1:
                if num < 0:
                    count += n - bisect_left(nums2, ceil(target / num))
                elif num == 0:
                    if target >= 0:
                        count += n
                else:
                    count += bisect_right(nums2, target // num)
            return count

        left = -(10**10)
        right = 10**10
        while left < right:
            mid = (left + right) // 2
            products = count_products_leq_target(mid)
            if products >= k:
                right = mid
            else:
                left = mid + 1
        return left
