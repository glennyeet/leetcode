class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        i = 1
        prev_lps = 0
        while i < len(needle):
            if needle[prev_lps] == needle[i]:
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            elif prev_lps == 0:
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
        haystack_index = 0
        needle_index = 0
        while haystack_index < len(haystack):
            if haystack[haystack_index] == needle[needle_index]:
                needle_index += 1
                haystack_index += 1
            elif needle_index == 0:
                haystack_index += 1
            else:
                needle_index = lps[needle_index - 1]
            if needle_index == len(needle):
                return haystack_index - len(needle)
        return -1
