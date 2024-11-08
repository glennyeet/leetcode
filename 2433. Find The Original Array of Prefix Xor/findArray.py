class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        arr_xor_sum = 0
        for num in pref:
            arr.append(arr_xor_sum ^ num)
            arr_xor_sum ^= arr[-1]
        return arr
