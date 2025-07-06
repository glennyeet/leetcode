from typing import List
from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_counter = Counter(nums1)
        self.nums2 = nums2
        self.nums2_counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1_counter:
            count += self.nums1_counter[num] * self.nums2_counter[tot - num]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
