from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        # String: O(n * c) time, O(n) space, where c is the size of the largest
        # string in code

        n = len(code)
        valid_coupons = []
        valid_categories = ["electronics", "grocery", "pharmacy", "restaurant"]

        def is_valid_code(code: str) -> bool:
            if len(code) == 0:
                return False
            for char in code:
                if not char.isalnum() and char != "_":
                    return False
            return True

        for i in range(n):
            if (
                is_valid_code(code[i])
                and businessLine[i] in valid_categories
                and isActive[i]
            ):
                valid_coupons.append((code[i], businessLine[i]))
        valid_coupons.sort(key=lambda c: (c[1], c[0]))
        valid_codes = []
        for code, _ in valid_coupons:
            valid_codes.append(code)
        return valid_codes
