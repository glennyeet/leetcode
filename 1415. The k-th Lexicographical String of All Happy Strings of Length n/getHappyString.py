class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Backtracking: O(2^n) time, O(2^n) space

        letters = ["a", "b", "c"]
        happy_strings = []

        def get_kth_happy_string(cur_index: int, happy_string: list[str]) -> None:
            if cur_index == n:
                happy_strings.append("".join(happy_string))
                return
            for letter in letters:
                if len(happy_string) and happy_string[-1] == letter:
                    continue
                happy_string.append(letter)
                get_kth_happy_string(cur_index + 1, happy_string)
                happy_string.pop()

        get_kth_happy_string(0, [])
        if len(happy_strings) < k:
            return ""
        else:
            return happy_strings[k - 1]
