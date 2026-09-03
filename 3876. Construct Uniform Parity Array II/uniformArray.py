class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Math: O(n) time, O(1) space, where n is the
        # size of nums1

        is_all_even = all(num % 2 == 0 for num in nums1)
        if is_all_even:
            return True
        is_all_odd = all(num % 2 == 1 for num in nums1)
        if is_all_odd:
            return True
        min_odd_num = float("inf")
        for num in nums1:
            if num % 2 == 1:
                min_odd_num = min(min_odd_num, num)
        can_make_even_array = True
        for num in nums1:
            if num % 2 == 1 and num - min_odd_num < 1:
                can_make_even_array = False
                break
        can_make_odd_array = True
        for num in nums1:
            if num % 2 == 0 and num - min_odd_num < 1:
                can_make_odd_array = False
                break
        return can_make_even_array or can_make_odd_array
