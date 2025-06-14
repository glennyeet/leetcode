class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Greedy: O(log(n)) time, O(log(n)) space,
        # where n is num

        num_str = str(num)
        remapped_min_digit = num_str[0]
        remapped_max_digit = None
        for i in range(len(num_str)):
            if num_str[i] != "9":
                remapped_max_digit = num_str[i]
                break
        max_value = []
        min_value = []
        for digit in num_str:
            if digit == remapped_max_digit:
                max_value.append("9")
            else:
                max_value.append(digit)
            if digit == remapped_min_digit:
                if min_value:
                    min_value.append("0")
            else:
                min_value.append(digit)
        if not min_value:
            min_value.append("0")
        return int("".join(max_value)) - int("".join(min_value))
