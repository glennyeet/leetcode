from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(list(s1))
        i = 0
        j = i + len(s1) - 1
        window_counter = Counter(list(s2[i : j + 1]))
        if window_counter == s1_counter:
            return True
        while True:
            j += 1
            if j >= len(s2):
                return False
            window_counter[s2[i]] -= 1
            i += 1
            window_counter[s2[j]] += 1
            if window_counter == s1_counter:
                return True
