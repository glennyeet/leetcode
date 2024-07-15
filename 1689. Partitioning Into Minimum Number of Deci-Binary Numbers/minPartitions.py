class Solution:
    def minPartitions(self, n: str) -> int:
        maxDigit = "0"
        for d in n:
            if d > maxDigit:
                maxDigit = d
        return int(maxDigit)
        # n = [int(d) for d in n]
        # return max(n)
