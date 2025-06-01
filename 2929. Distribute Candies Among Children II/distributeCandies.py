class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Enumeration: O(n) time, O(1) space

        ways = 0
        for i in range(min(n, limit) + 1):
            candies_left = n - i
            if candies_left <= limit * 2:
                ways += min(candies_left, limit * 2 - candies_left) + 1
        return ways
