class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_int = ""
        for c in s:
            s_int += str(ord(c) - 96)
        for _ in range(k):
            s_sum = 0
            for c in s_int:
                s_sum += int(c)
            s_int = str(s_sum)
        return s_sum
