class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Backtracking: O(n * 2^(log(n))) time, O(log(n)) space

        def is_valid_square(
            num_str: str, target_sum: int, cur_index: int, cur_sum: int
        ) -> bool:
            num_len = len(num_str)
            if cur_index == num_len and cur_sum == target_sum:
                return True
            for i in range(cur_index, num_len):
                if is_valid_square(
                    num_str,
                    target_sum,
                    i + 1,
                    cur_sum + int(num_str[cur_index : i + 1]),
                ):
                    return True
            return False

        punishment_number = 0
        for i in range(1, n + 1):
            square = i**2
            if is_valid_square(str(square), i, 0, 0):
                punishment_number += square
        return punishment_number
