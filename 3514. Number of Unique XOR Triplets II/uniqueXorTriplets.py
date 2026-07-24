from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Bit Manipulation + Hash Table: O(n) time,
        # O(n) space

        n = len(nums)
        one_element = set()
        two_elements = set()
        three_elements = set()
        for i in range(n):
            num1 = nums[i]
            one_element.add(num1)
            for num2 in one_element:
                two_elements.add(num1 ^ num2)
            for num2 in two_elements:
                three_elements.add(num1 ^ num2)
        return len(three_elements)
