class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Counting: O(n) time, O(1) space, where n
        # is the size of text

        letter_counter = [0] * 5  # a, b, l, o, n
        for char in text:
            match char:
                case "a":
                    letter_counter[0] += 1
                case "b":
                    letter_counter[1] += 1
                case "l":
                    letter_counter[2] += 1
                case "o":
                    letter_counter[3] += 1
                case "n":
                    letter_counter[4] += 1
        letter_counter[2] //= 2
        letter_counter[3] //= 2
        return min(letter_counter)
