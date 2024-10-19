class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse_invert_string(string: str) -> str:
            new_string = ""
            for c in string:
                if c == "0":
                    new_string += "1"
                else:
                    new_string += "0"
            return new_string[::-1]

        binary_string = "0"
        for _ in range(n - 1):
            binary_string = binary_string + "1" + reverse_invert_string(binary_string)
        return binary_string[k - 1]
