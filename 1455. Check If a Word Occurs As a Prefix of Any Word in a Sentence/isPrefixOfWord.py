class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        search_prefix = " " + searchWord
        m = len(search_prefix)
        lps = [0] * m
        prev_lps = 0
        i = 1
        while i < m:
            if search_prefix[i] == search_prefix[prev_lps]:
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            elif prev_lps == 0:
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
        search_sentence = " " + sentence
        n = len(search_sentence)
        word_count = 0
        i = 0
        j = 0
        while j < n:
            if search_sentence[j] == search_prefix[i]:
                if search_sentence[j] == " ":
                    word_count += 1
                i += 1
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]
            if i == m:
                return word_count
        return -1
