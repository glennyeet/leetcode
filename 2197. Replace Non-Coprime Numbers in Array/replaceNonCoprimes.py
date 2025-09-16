from typing import List
from collections import deque
from math import gcd, lcm


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # Math + Stack + Deque: O(n) time, O(n) space, where n is
        # the size of nums

        adjacent_coprimes = []
        unprocessed_nums = deque(nums)
        while unprocessed_nums:
            if not adjacent_coprimes:
                adjacent_coprimes.append(unprocessed_nums.popleft())
            else:
                x = adjacent_coprimes[-1]
                y = unprocessed_nums[0]
                if gcd(x, y) > 1:
                    adjacent_coprimes.pop()
                    unprocessed_nums.popleft()
                    unprocessed_nums.appendleft(lcm(x, y))
                else:
                    unprocessed_nums.popleft()
                    adjacent_coprimes.append(y)
        return adjacent_coprimes
