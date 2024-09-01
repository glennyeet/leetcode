class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        two_d_array = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            m_index = i // n
            n_index = i % n
            two_d_array[m_index][n_index] = original[i]
        return two_d_array
