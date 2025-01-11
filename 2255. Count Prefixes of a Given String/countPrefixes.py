class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        # Brute force: O(nm) time, O(1) space, where n is the
        # number of words and m is the length of the longest
        # word in words

        valid_strings = 0
        for word in words:
            if s.startswith(word):
                valid_strings += 1
        return valid_strings
