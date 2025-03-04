class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # Backtracking: O(n) time, O(log_3(n)) space

        def is_powers_of_three_sum(cur_sum: int, exponent: int) -> bool:
            cur_power = 3**exponent
            if cur_sum == n:
                return True
            elif cur_sum > n or cur_power > n:
                return False
            if is_powers_of_three_sum(cur_sum + cur_power, exponent + 1):
                return True
            return is_powers_of_three_sum(cur_sum, exponent + 1)

        return is_powers_of_three_sum(0, 0)
