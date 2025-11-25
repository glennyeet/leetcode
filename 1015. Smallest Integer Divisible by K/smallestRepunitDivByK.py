class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Hash Table + Math: O(k) time, O(k) space

        remainders = set()
        remainder = 0
        min_length = 0
        while remainder not in remainders:
            remainders.add(remainder)
            remainder = (remainder * 10 + 1) % k
            min_length += 1
            if remainder == 0:
                return min_length
        return -1
