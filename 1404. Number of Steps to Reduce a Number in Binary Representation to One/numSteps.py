class Solution:
    def numSteps(self, s: str) -> int:
        # Greedy: O(n) time, O(n) space,
        # where n is the size of s

        steps = 0
        cur_num = int("0b" + s, 2)
        while cur_num != 1:
            steps += 1
            if cur_num % 2:
                cur_num += 1
            else:
                cur_num //= 2
        return steps
