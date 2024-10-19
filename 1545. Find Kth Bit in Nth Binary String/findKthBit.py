class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Brute Force
        # def reverse_invert_string(string: str) -> str:
        #     new_string = ""
        #     for c in string:
        #         if c == "0":
        #             new_string += "1"
        #         else:
        #             new_string += "0"
        #     return new_string[::-1]

        # binary_string = "0"
        # for _ in range(n - 1):
        #     binary_string = binary_string + "1" + reverse_invert_string(binary_string)
        # return binary_string[k - 1]

        # Recursion
        length = 2**n - 1

        def get_bit(length: int, k: int) -> str:
            if length == 1:
                return "0"
            mid = length // 2
            if k == mid + 1:
                return "1"
            if k <= mid:
                return get_bit(mid, k)
            elif k > mid + 1:
                bit = get_bit(mid, length + 1 - k)
                if bit == "0":
                    return "1"
                else:
                    return "0"

        return get_bit(length, k)
