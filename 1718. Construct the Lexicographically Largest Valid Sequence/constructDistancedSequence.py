class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Backtracking: O(n!) time, O(n) space

        sequence_len = 2 * n - 1
        sequence = [0] * sequence_len
        used_integers = set()

        def build_sequence(cur_index: int) -> bool:
            if cur_index == sequence_len:
                return True
            for num in reversed(range(1, n + 1)):
                if num in used_integers:
                    continue
                if num > 1 and (
                    cur_index + num >= sequence_len or sequence[cur_index + num]
                ):
                    continue
                used_integers.add(num)
                sequence[cur_index] = num
                if num > 1:
                    sequence[cur_index + num] = num
                next_index = cur_index + 1
                while next_index < sequence_len and sequence[next_index]:
                    next_index += 1
                if build_sequence(next_index):
                    return True
                used_integers.remove(num)
                sequence[cur_index] = 0
                if num > 1:
                    sequence[cur_index + num] = 0
            return False

        build_sequence(0)
        return sequence
