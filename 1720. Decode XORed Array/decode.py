class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        prev_num = first
        for num in encoded:
            prev_num ^= num
            arr.append(prev_num)
        return arr
