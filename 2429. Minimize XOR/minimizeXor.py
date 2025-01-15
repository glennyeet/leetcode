class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Greedy: O(log(n)) time, O(1) space, where
        # n = max(num1, num2)

        num2_set_bits = num2.bit_count()
        x = 0
        for i in reversed(range(32)):
            if num2_set_bits > 0 and num1 & 1 << i > 0:
                x |= 1 << i
                num2_set_bits -= 1
        for i in range(32):
            if num2_set_bits > 0 and num1 & 1 << i == 0:
                x |= 1 << i
                num2_set_bits -= 1
        return x
