class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_num = arrays[0][0]
        max_num = arrays[0][-1]
        max_distance = 0
        for i in range(1, len(arrays)):
            local_min = arrays[i][0]
            local_max = arrays[i][-1]
            max_distance = max(
                max_distance, abs(local_min - max_num), abs(local_max - min_num)
            )
            min_num = min(min_num, local_min)
            max_num = max(max_num, local_max)
        return max_distance
