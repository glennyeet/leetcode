class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        num_to_rank = {}
        rank = 0
        prev = None
        for num in sorted_arr:
            if num != prev:
                rank += 1
            num_to_rank[num] = rank
            prev = num
        ranks = []
        for num in arr:
            ranks.append(num_to_rank[num])
        return ranks
