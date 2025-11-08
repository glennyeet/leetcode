class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Math + Recursion: O(log(n)^2) time, O(log(n)) space

        def count_operations(num: int) -> int:
            if num == 0:
                return 0
            k = 0
            while 2**k <= num:
                k += 1
            k -= 1
            return 2 ** (k + 1) - 1 - count_operations(2**k ^ num)

        return count_operations(n)
