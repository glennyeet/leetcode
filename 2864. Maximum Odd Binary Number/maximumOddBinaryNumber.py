class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeroes_count = 0
        ones_count = 0
        for c in s:
            if c == "0":
                zeroes_count += 1
            else:
                ones_count += 1
        if ones_count > 0:
            leading_ones = "1" * (ones_count - 1)
        else:
            leading_ones = ""
        max_odd_num = leading_ones + "0" * zeroes_count + "1"
        return max_odd_num
