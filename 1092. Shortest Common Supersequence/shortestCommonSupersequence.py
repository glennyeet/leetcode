class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Bottom-up DP: O(m * n * (m + n)) time, O(n * (m + n)) space

        m = len(str1)
        n = len(str2)
        prev = []
        for j in range(n):
            prev.append(str2[j:])
        prev.append("")
        for i in reversed(range(m)):
            cur = [""] * n
            cur.append(str1[i:])
            for j in reversed(range(n)):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prev[j + 1]
                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + cur[j + 1]
                    if len(res1) < len(res2):
                        cur[j] = res1
                    else:
                        cur[j] = res2
            prev = cur
        return cur[0]
