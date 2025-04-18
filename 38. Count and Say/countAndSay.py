class Solution:
    def countAndSay(self, n: int) -> str:
        def get_encoding(nth: int, encoding: str) -> str:
            # Recursion: O(2^n) time, O(2^n) space

            if nth == n:
                return encoding
            new_encoding = []
            streak_digit = encoding[0]
            streak = 0
            e = len(encoding)
            for i in range(e + 1):
                if i == e:
                    new_encoding.append(str(streak) + streak_digit)
                    break
                if encoding[i] != streak_digit:
                    new_encoding.append(str(streak) + streak_digit)
                    streak_digit = encoding[i]
                    streak = 0
                streak += 1
            return get_encoding(nth + 1, "".join(new_encoding))

        return get_encoding(1, "1")
