class Solution:
    def minPartitions(self, n: str) -> int:
        maxDigit = -1
        for d in n:
            if int(d) > maxDigit:
                maxDigit = int(d)
        return maxDigit
        # n = [int(d) for d in n]
        # return max(n)
