from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        # Simulation: O(n * log(n)) time, O(n) space

        n = len(nums)
        mx = 0
        prefix_gcd = []
        for num in nums:
            mx = max(mx, num)
            prefix_gcd.append(gcd(num, mx))
        prefix_gcd.sort()
        gcd_sum = 0
        i = 0
        j = n - 1
        while i < j:
            gcd_sum += gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1
        return gcd_sum
