class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding Window: O(m + n) time, O(1) space

        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        s1_counter = [0] * 26
        for char in s1:
            s1_counter[ord(char) - ord("a")] += 1
        right = 0
        substring_counter = [0] * 26
        for left in range(n - m + 1):
            while right - left < m:
                substring_counter[ord(s2[right]) - ord("a")] += 1
                right += 1
            if s1_counter == substring_counter:
                return True
            substring_counter[ord(s2[left]) - ord("a")] -= 1
        return False
