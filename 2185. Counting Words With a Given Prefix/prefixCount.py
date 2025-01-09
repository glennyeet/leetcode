class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Brute force: O(np) time, O(1) space, where n is the
        # number of words and p is the length of the prefix

        valid_words = 0
        for word in words:
            if word.startswith(pref):
                valid_words += 1
        return valid_words
