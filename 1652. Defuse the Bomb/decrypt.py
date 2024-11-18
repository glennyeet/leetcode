class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted_code = [0] * n
        if k > 0:
            decrypted_code[-1] = sum(code[:k])
            l = n - 2
            r = k - 1
            while l >= 0:
                decrypted_code[l] = decrypted_code[l + 1] + code[l + 1] - code[r]
                l -= 1
                r = (r - 1) % n
        elif k < 0:
            decrypted_code[0] = sum(code[n + k :])
            l = n + k
            r = 1
            while r < n:
                decrypted_code[r] = decrypted_code[r - 1] + code[r - 1] - code[l]
                l = (l + 1) % n
                r += 1
        return decrypted_code
