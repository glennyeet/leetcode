class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        same_parity_pairs_sum = [0]

        def is_parity_same(num1: int, num2: int) -> int:
            return num1 & 1 ^ num2 & 1 ^ 1

        for i in range(1, len(nums)):
            same_parity_pairs_sum.append(
                same_parity_pairs_sum[i - 1] + is_parity_same(nums[i - 1], nums[i])
            )
        answer = []
        for from_index, to_index in queries:
            answer.append(
                same_parity_pairs_sum[to_index] - same_parity_pairs_sum[from_index] == 0
            )
        return answer
