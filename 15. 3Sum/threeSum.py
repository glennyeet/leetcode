from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two Pointers + Hash Table: O(n^2) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        triplets = []
        triplets_set = set()
        for k in range(n):
            i = 0
            j = k - 1
            while i < j:
                cur_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                triplet = (sorted_nums[i], sorted_nums[j], sorted_nums[k])
                if triplet not in triplets_set and cur_sum == 0:
                    triplets.append(list(triplet))
                    triplets_set.add(triplet)
                if cur_sum <= 0:
                    i += 1
                else:
                    j -= 1
        return triplets
