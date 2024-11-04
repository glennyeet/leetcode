class Solution:
    def compressedString(self, word: str) -> str:
        cur_char = word[0]
        char_count = 0
        comp = []
        for c in word:
            if c == cur_char and char_count < 9:
                char_count += 1
            else:
                comp.append(str(char_count) + cur_char)
                cur_char = c
                char_count = 1
        comp.append(str(char_count) + cur_char)
        return "".join(comp)
