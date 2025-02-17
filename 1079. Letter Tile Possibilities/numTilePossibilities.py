from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Backtracking: O(2^n) time, O(n) space, where
        # n is the size of tiles
        tiles_counter = Counter(tiles)

        def count_sequences() -> int:
            sequences = 0
            for tile in tiles_counter:
                if not tiles_counter[tile]:
                    continue
                tiles_counter[tile] -= 1
                sequences += 1 + count_sequences()
                tiles_counter[tile] += 1
            return sequences

        return count_sequences()
