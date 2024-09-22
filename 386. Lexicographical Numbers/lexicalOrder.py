import math


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        numbers = []
        n_digits = math.floor(math.log10(n) + 1)
        start = 10 ** (n_digits - 1)

        def generate_numbers(start: int, end: int):
            for x in range(start, end + 1):
                # First pass: 10^(n_digits - 1) to n
                # Second pass: n // 10 + 1 to 10^(n_digits - 1) - 1
                numbers.append(x)
                # quotients of any number divisible by 10, e.g. 100 -> 1, 10
                count = 0
                while x % 10 == 0:
                    x //= 10
                    count += 1
                    numbers.append(x)
                left = len(numbers) - count - 1
                right = len(numbers) - 1
                while left < right:
                    numbers[left], numbers[right] = numbers[right], numbers[left]
                    left += 1
                    right -= 1

        generate_numbers(start, n)
        generate_numbers(n // 10 + 1, start - 1)

        return numbers
