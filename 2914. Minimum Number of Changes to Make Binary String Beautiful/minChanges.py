class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        cur_bit = None
        cur_bit_count = 0
        for bit in s:
            if bit != cur_bit:
                if cur_bit_count % 2:
                    changes += 1
                    cur_bit_count = 0
                else:
                    cur_bit = bit
                    cur_bit_count = 1
            else:
                cur_bit_count += 1
        return changes
