class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Backtracking: O(2^n) time, O(2^n) space

        happy_strings = []

        def generate_all_happy_strings(cur_string: str) -> None:
            if len(cur_string) == n:
                happy_strings.append(cur_string)
                return
            next_char = ["a", "b", "c"]
            if cur_string:
                next_char.remove(cur_string[-1])
            for char in next_char:
                generate_all_happy_strings(cur_string + char)

        generate_all_happy_strings("")
        if len(happy_strings) < k:
            return ""
        happy_strings.sort()
        return happy_strings[k - 1]
