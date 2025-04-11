class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # Brute force: O(alog(a)) time, O(1) space, where
        # a = high - low + 1

        symmetric_integers = 0
        for num in range(low, high + 1):
            num_str = str(num)
            m = len(num_str)
            if m % 2:
                continue
            n = m // 2
            left_sum = 0
            for i in range(0, n):
                left_sum += int(num_str[i])
            right_sum = 0
            for i in range(n, m):
                right_sum += int(num_str[i])
            symmetric_integers += left_sum == right_sum
        return symmetric_integers
