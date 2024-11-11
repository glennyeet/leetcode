from math import sqrt


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime_check = {}

        def is_prime(num: int) -> bool:
            if num in prime_check:
                return prime_check[num]
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    prime_check[num] = False
                    return False
            prime_check[num] = True
            return True

        prev_num = 0
        for num in nums:
            new_num = num
            max_p = num - prev_num - 1
            for p in range(max_p, 1, -1):
                if is_prime(p):
                    new_num = num - p
                    break
            if new_num <= prev_num:
                return False
            prev_num = new_num
        return True
