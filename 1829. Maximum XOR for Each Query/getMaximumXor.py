class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        max_k = 0
        for i in range(maximumBit):
            max_k |= 1 << i
        while nums:
            k = xor_sum ^ max_k
            answer.append(k)
            xor_sum ^= nums.pop()
            i += 1
        return answer
