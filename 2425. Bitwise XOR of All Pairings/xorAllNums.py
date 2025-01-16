class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Bit manipulation: O(m + n) time, O(1) space

        m = len(nums1)
        n = len(nums2)
        xor_sum = 0
        if n % 2 == 1:
            for num in nums1:
                xor_sum ^= num
        if m % 2 == 1:
            for num in nums2:
                xor_sum ^= num
        return xor_sum
