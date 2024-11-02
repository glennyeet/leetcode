class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        cur_word = words[0]
        prev_word = words[len(words) - 1]
        if cur_word[0] != prev_word[len(prev_word) - 1]:
            return False
        for i in range(1, len(words)):
            cur_word = words[i]
            prev_word = words[i - 1]
            if cur_word[0] != prev_word[len(prev_word) - 1]:
                return False
        return True
