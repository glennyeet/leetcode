class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        cache = []
        xor = arr[0]
        cache.append(xor)
        for i in range(1, len(arr)):
            xor ^= arr[i]
            cache.append(xor)
        for left, right in queries:
            if left == 0:
                answer.append(cache[right])
            else:
                answer.append(cache[left - 1] ^ cache[right])
        return answer
