class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        s1_words = sentence1.split(" ")
        s2_words = sentence2.split(" ")
        s1_len = len(s1_words)
        s2_len = len(s2_words)
        if s1_len == s2_len:
            return False
        if s1_len > s2_len:
            long_sentence = s1_words
            short_sentence = s2_words
        else:
            long_sentence = s2_words
            short_sentence = s1_words
        l_start = 0
        l_end = len(long_sentence) - 1
        s_start = 0
        s_end = len(short_sentence) - 1
        while s_start <= s_end:
            if (
                long_sentence[l_start] != short_sentence[s_start]
                and long_sentence[l_end] != short_sentence[s_end]
            ):
                return False
            if long_sentence[l_start] == short_sentence[s_start]:
                l_start += 1
                s_start += 1
            if long_sentence[l_end] == short_sentence[s_end]:
                l_end -= 1
                s_end -= 1
        return True
