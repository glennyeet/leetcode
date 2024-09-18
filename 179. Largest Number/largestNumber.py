from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def get_max_combo(num1: int, num2: int) -> int:
            if num1 == num2:
                return 0
            combo1 = int(str(num1) + str(num2))
            combo2 = int(str(num2) + str(num1))
            if combo2 > combo1:
                return 1
            else:
                return -1

        nums.sort(key=cmp_to_key(get_max_combo))
        return str(int("".join(map(str, nums))))
