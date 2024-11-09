class Solution:
    def minEnd(self, n: int, x: int) -> int:
        last_index = n - 1
        i_li = 1
        i_x = 1
        last_num = x
        while i_li <= last_index:
            if x & i_x == 0:
                if last_index & i_li:
                    last_num |= i_x
                i_li <<= 1
            i_x <<= 1
        return last_num
