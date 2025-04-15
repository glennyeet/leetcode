from typing import List


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        index += 1
        answer = 0
        while index > 0:
            answer += self.tree[index]
            index -= index & -index
        return answer


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Binary indexed tree: O(nlog(n)) time, O(n) space

        n = len(nums1)
        nums1_ordering = {}
        for i, num in enumerate(nums1):
            nums1_ordering[num] = i
        nums2_ordering = {}
        for i, num in enumerate(nums2):
            nums2_ordering[nums1_ordering[num]] = i
        fenwick_tree = FenwickTree(n)
        good_triplets = 0
        for value in range(n):
            position = nums2_ordering[value]
            left = fenwick_tree.query(position)
            fenwick_tree.update(position, 1)
            right = (n - 1 - position) - (value - left)
            good_triplets += left * right
        return good_triplets
