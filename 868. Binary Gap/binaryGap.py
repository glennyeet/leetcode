class Solution:
    def binaryGap(self, n: int) -> int:
        # Bit Manipulation: O(log(n)) time, O(1) space

        max_dist = 0
        cur_n = n
        cur_dist = 0
        prev_one = None
        while cur_n:
            if cur_n & 1:
                if prev_one is not None:
                    max_dist = max(max_dist, cur_dist - prev_one)
                prev_one = cur_dist
            cur_n >>= 1
            cur_dist += 1
        return max_dist
