class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Brute Force: O(n * log(m)) time, O(1) space,
        # where n is num2 - num1 and m is the the number
        # of digits in max([num1, num2])

        total_waviness = 0
        for num in range(num1, num2 + 1):
            num_str = str(num)
            for i in range(1, len(num_str) - 1):
                total_waviness += (
                    num_str[i - 1] < num_str[i]
                    and num_str[i + 1] < num_str[i]
                    or num_str[i - 1] > num_str[i]
                    and num_str[i + 1] > num_str[i]
                )
        return total_waviness
