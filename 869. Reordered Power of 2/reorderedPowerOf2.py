class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Hash Table: O(1) time, O(1) space

        def sort_digits(num: int) -> str:
            return "".join(sorted(str(num)))

        powers_of_two = set()
        for i in range(32):
            power_of_two = 2**i
            powers_of_two.add(sort_digits(power_of_two))
        return sort_digits(n) in powers_of_two
