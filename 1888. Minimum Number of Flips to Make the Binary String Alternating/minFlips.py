class Solution:
    def minFlips(self, s: str) -> int:
        # Prefix Sum + Sliding Window: O(n) time, O(n) space

        bits = []
        for bit in s:
            bits.append(int(bit))
        bits = bits * 2
        inverted_bits = []
        for bit in bits:
            inverted_bits.append(1 - bit)

        def get_min_operations(bits: list[int]) -> int:
            n = len(bits) // 2
            prefix_diffs = [0]
            min_operations = n
            for i, bit in enumerate(bits):
                if i % 2 == bit:
                    prefix_diffs.append(prefix_diffs[-1])
                else:
                    prefix_diffs.append(prefix_diffs[-1] + 1)
                if i >= n:
                    min_operations = min(
                        min_operations, prefix_diffs[i] - prefix_diffs[i - n]
                    )
            return min_operations

        return min(get_min_operations(bits), get_min_operations(inverted_bits))
