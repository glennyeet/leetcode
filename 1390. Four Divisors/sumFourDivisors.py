from typing import List
from math import ceil, sqrt


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # Math: O(n * √n) time, O(1) space, where n is
        # the size of nums

        def find_divisor_sum(product: int) -> int:
            stop_num = ceil(sqrt(product))
            if stop_num**2 == product:
                return 0
            has_four_divisors = False
            divisor_sum = 1 + product
            for num in range(2, stop_num):
                if product % num == 0:
                    if not has_four_divisors:
                        has_four_divisors = True
                        divisor_sum += num + product // num
                    else:
                        has_four_divisors = False
                        break
            if not has_four_divisors:
                return 0
            else:
                return divisor_sum

        total_divisor_sum = 0
        for num in nums:
            total_divisor_sum += find_divisor_sum(num)
        return total_divisor_sum
