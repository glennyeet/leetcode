# from collections import defaultdict


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Dictionary
        # counter = defaultdict(int)
        # for c in allowed:
        #     counter[c] += 1
        # consistent_strings = 0
        # for word in words:
        #     allowed_string = 1
        #     for c in word:
        #         if counter[c] == 0:
        #             allowed_string = 0
        #             break
        #     consistent_strings += allowed_string
        # return consistent_strings

        # Set
        # allowed_set = set(allowed)
        # consistent_strings = 0
        # for word in words:
        #     allowed_string = 1
        #     for c in word:
        #         if c not in allowed_set:
        #             allowed_string = 0
        #             break
        #     consistent_strings += allowed_string
        # return consistent_strings

        # Bitmask
        bitmask = 0
        for c in allowed:
            bitmask |= 1 << ord(c) - ord("a")
        consistent_strings = len(words)
        for word in words:
            for c in word:
                if not bitmask >> ord(c) - ord("a") & 1:
                    consistent_strings -= 1
                    break
        return consistent_strings
