from math import isqrt


class Solution:

    def sortableIntegers(self, nums: list[int]) -> int:
        # KMP: O(n * √n) time, O(n) space

        n = len(nums)
        factors = []
        for num in range(1, isqrt(n) + 1):
            if n % num == 0:
                factors.append(num)
                if n // num != num:
                    factors.append(n // num)
        sorted_nums = sorted(nums)

        def kmp(nums1: list[int], nums2: list[int]) -> bool:
            n1 = len(nums1)
            n2 = len(nums2)
            lps = [0] * n2
            j = 0
            for i in range(1, n2):
                while j > 0 and nums2[i] != nums2[j]:
                    j = lps[j - 1]
                if nums2[i] == nums2[j]:
                    j += 1
                lps[i] = j
            j = 0
            for i in range(n1):
                while j > 0 and nums1[i] != nums2[j]:
                    j = lps[j - 1]
                if nums1[i] == nums2[j]:
                    j += 1
                if j == n2:
                    return True
            return False

        ans = 0
        for divisor in factors:
            for left in range(0, n, divisor):
                right = left + divisor - 1
                if not kmp(
                    nums[left : right + 1] + nums[left : right + 1],
                    sorted_nums[left : right + 1],
                ):
                    break
            else:
                ans += divisor
        return ans
