class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Math: O(n) time, O(1) space

        possible_pairs = 0
        even_y = m // 2
        odd_y = m // 2 + m % 2
        for x in range(1, n + 1):
            if x % 2 == 0:
                possible_pairs += odd_y
            else:
                possible_pairs += even_y
        return possible_pairs
