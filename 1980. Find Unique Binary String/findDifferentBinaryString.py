class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Backtracking: O(2^n) time, O(2^n) space

        # n = len(nums)
        # characters = ["0", "1"]
        # binary_strings = []

        # def get_binary_strings(cur_index: int, binary_string: list[str]) -> None:
        #     if cur_index == n:
        #         binary_strings.append("".join(binary_string))
        #         return
        #     for char in characters:
        #         binary_string.append(char)
        #         get_binary_strings(cur_index + 1, binary_string)
        #         binary_string.pop()

        # get_binary_strings(0, [])
        # nums_set = set(nums)
        # for binary_string in binary_strings:
        #     if binary_string not in nums_set:
        #         return binary_string

        # Backtracking: O(n^2) time, O(n) space

        # n = len(nums)
        # characters = ["0", "1"]
        # nums_set = set(nums)

        # def get_binary_string(cur_index: int, binary_string_list: list[str]) -> str:
        #     if cur_index == n:
        #         binary_string = "".join(binary_string_list)
        #         if binary_string not in nums_set:
        #             return binary_string
        #         return ""
        #     for char in characters:
        #         binary_string_list.append(char)
        #         binary_string = get_binary_string(cur_index + 1, binary_string_list)
        #         if binary_string:
        #             return binary_string
        #         binary_string_list.pop()

        # return get_binary_string(0, [])

        # Cantor's Diagonal Argument: O(n) time, O(n) space

        n = len(nums)
        binary_string = []
        for i in range(n):
            if nums[i][i] == "0":
                binary_string.append("1")
            else:
                binary_string.append("0")
        return "".join(binary_string)
