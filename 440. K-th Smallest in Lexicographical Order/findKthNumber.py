class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        answer = 1
        i = 1

        def get_subtree_size(step: int) -> int:
            size = 0
            neighbour = step + 1
            while step <= n:
                size += min(neighbour, n + 1) - step
                step *= 10
                neighbour *= 10
            return size

        while i < k:
            subtree_size = get_subtree_size(answer)
            if i + subtree_size <= k:
                answer += 1
                i += subtree_size
            else:
                answer *= 10
                i += 1
        return answer
