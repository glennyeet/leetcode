class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Greedy: O(n) time, O(n) space

        n = len(s)
        active_sections = s.count("1")
        inactive_blocks = []
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            if s[start] == "0":
                inactive_blocks.append(i - start)
        z = len(inactive_blocks)
        if z < 2:
            return active_sections
        max_new_active_sections = 0
        for i in range(z - 1):
            max_new_active_sections = max(
                max_new_active_sections, inactive_blocks[i] + inactive_blocks[i + 1]
            )
        return active_sections + max_new_active_sections
