class Solution:
    def maxDiff(self, num: int) -> int:
        # Greedy: O(log(n)) time, O(1) space,
        # where n is num

        num_str = str(num)
        max_value = num
        for digit in num_str:
            if digit != "9":
                max_value = int(num_str.replace(digit, "9"))
                break
        min_value = num
        for i, digit in enumerate(num_str):
            if i == 0:
                if digit != "1":
                    min_value = int(num_str.replace(digit, "1"))
                    break
            else:
                if digit != num_str[0] and digit != "0":
                    min_value = int(num_str.replace(digit, "0"))
                    break
        return max_value - min_value
