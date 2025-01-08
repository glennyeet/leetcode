class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # Brute force: O(n^2 * m) time, O(1) space, where m is
        # the length of the longest word

        n = len(words)
        prefix_suffix_pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    prefix_suffix_pairs += 1
        return prefix_suffix_pairs
