from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Sliding Window + Bit Manipulation: O(n) time, O(n) space

        n = len(nums)
        bit_counts = [0] * 32
        cur_or = 0
        max_or = 0
        min_lengths = [0] * n
        right = n - 1
        for left in reversed(range(n)):
            for i in range(32):
                if nums[left] & 1 << i:
                    bit_counts[i] += 1
                    cur_or |= 1 << i
            max_or |= nums[left]
            while cur_or == max_or and left <= right:
                for i in range(32):
                    if nums[right] & 1 << i:
                        bit_counts[i] -= 1
                        if not bit_counts[i]:
                            cur_or ^= 1 << i
                right -= 1
            min_lengths[left] = right - left + 2
        return min_lengths
