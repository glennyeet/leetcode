class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Greedy: O(n^2) time, O(n) space, where
        # n is the size of pattern

        # number = [1]
        # for c in pattern:
        #     if c == "I":
        #         i = 1
        #         while i in number:
        #             i += 1
        #         number.append(i)
        #     else:
        #         number.append(number[-1])
        #         i = len(number) - 2
        #         while i >= 0 and number[i] == number[i + 1]:
        #             number[i] += 1
        #             i -= 1
        # number = "".join([str(d) for d in number])
        # return number

        # Brute force: O(n! * n^2) time, O(n!) space

        n = len(pattern)
        permutations = []

        def get_possible_strings(start_index: int, num: list[str]) -> None:
            string_len = len(num)
            if start_index == string_len:
                permutations.append("".join(num))
                return
            for i in range(start_index, string_len):
                num[start_index], num[i] = num[i], num[start_index]
                get_possible_strings(start_index + 1, num)
                num[start_index], num[i] = num[i], num[start_index]

        num = []
        for i in range(1, n + 2):
            num.append(str(i))
        get_possible_strings(0, num)

        def is_valid_string(num: list[str]) -> bool:
            for i in range(n):
                if (
                    pattern[i] == "I"
                    and num[i] >= num[i + 1]
                    or pattern[i] == "D"
                    and num[i] <= num[i + 1]
                ):
                    return False
            return True

        for num in permutations:
            if is_valid_string(num):
                return num
