class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Divide and Conquer: O(n^2) time, O(n^2) space, where n is the size
        # of s

        def get_largest_string(substring: str) -> str:
            largest_string = []
            ones = 0
            i = 0
            for j, bit in enumerate(substring):
                if bit == "1":
                    ones += 1
                else:
                    ones -= 1
                if ones == 0:
                    largest_string.append(
                        "1" + get_largest_string(substring[i + 1 : j]) + "0",
                    )
                    i = j + 1
            return "".join(sorted(largest_string, reverse=True))

        return get_largest_string(s)
