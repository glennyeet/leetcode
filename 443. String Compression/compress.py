class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            cur_char = chars[i]
            char_count = 1
            while i + 1 < len(chars) and chars[i + 1] == cur_char:
                char_count += 1
                chars.pop(i + 1)
            if char_count > 1:
                char_count_str = str(char_count)
                for c in char_count_str:
                    chars.insert(i + 1, c)
                    i += 1
            i += 1
        return len(chars)
