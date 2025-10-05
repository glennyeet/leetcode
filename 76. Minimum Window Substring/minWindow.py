from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Hash Table + Sliding Window: O(m + n) time, O(1) space

        m = len(s)
        n = len(t)
        if n > m:
            return ""
        t_counter = Counter(t)
        substring_counter = Counter()
        t_chars = len(t_counter)
        substring_chars = 0
        left = 0
        min_left = None
        min_right = None
        for right in range(m):
            substring_counter[s[right]] += 1
            if substring_counter[s[right]] == t_counter[s[right]]:
                substring_chars += 1
            while substring_chars == t_chars:
                if min_left == None or right - left + 1 < min_right - min_left + 1:
                    min_left = left
                    min_right = right
                substring_counter[s[left]] -= 1
                if substring_counter[s[left]] < t_counter[s[left]]:
                    substring_chars -= 1
                left += 1
        if min_left == None:
            return ""
        else:
            return s[min_left : min_right + 1]
