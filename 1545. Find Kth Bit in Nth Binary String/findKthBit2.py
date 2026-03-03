class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Simulation: O(2^n) time, O(2^n) space

        cur_s = "0"
        for _ in range(n):
            prev_s = cur_s
            inverted_s = []
            for bit in prev_s:
                if bit == "0":
                    inverted_s.append("1")
                else:
                    inverted_s.append("0")
            inverted_s = "".join(reversed(inverted_s))
            cur_s = prev_s + "1" + inverted_s
        return cur_s[k - 1]
