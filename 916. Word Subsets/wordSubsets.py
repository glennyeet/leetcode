from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Hash map: O(n + m) time, O(a) space, where n is the
        # number of words in words1, m is the number of words in words2,
        # a is the size of the answer array universal_strings

        words2_counter = Counter()
        for word in words2:
            word2_counter = Counter(word)
            for char in word2_counter:
                words2_counter[char] = max(words2_counter[char], word2_counter[char])
        universal_strings = []
        for word in words1:
            word1_counter = Counter(word)
            is_universal = True
            for char in words2_counter:
                if words2_counter[char] > word1_counter[char]:
                    is_universal = False
                    break
            if is_universal:
                universal_strings.append(word)
        return universal_strings
