from math import comb


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        # Divide and Conquer: O(n^2) time, O(n) space

        mod_factor = 10**9 + 7

        def find(subarray: list[int]) -> int:
            m = len(subarray)
            if m <= 2:
                return 1
            root = subarray[0]
            left = []
            right = []
            for i in range(1, m):
                if subarray[i] < root:
                    left.append(subarray[i])
                else:
                    right.append(subarray[i])
            return (
                find(left)
                * find(right)
                % mod_factor
                * comb(m - 1, len(left))
                % mod_factor
            )

        return (find(nums) - 1) % mod_factor
