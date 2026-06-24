def matmul(A: list[list[int]], B: list[list[int]], mod=None) -> list[list[int]]:
    n = len(A)
    m = len(B)
    p = len(B[0])
    result = [[0] * p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if A[i][k] == 0:
                continue
            for j in range(p):
                val = A[i][k] * B[k][j]
                if mod:
                    val %= mod
                    result[i][j] = (result[i][j] + val) % mod
                else:
                    result[i][j] += val
    return result


def matpow(M: list[list[int]], power: int, mod=None) -> list[list[int]]:
    n = len(M)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = [row[:] for row in M]
    while power > 0:
        if power & 1:
            result = matmul(result, base, mod)
        base = matmul(base, base, mod)
        power >>= 1
    return result


def vecmul(v: list[int], M: list[list[int]], mod=None) -> list[int]:
    n = len(v)
    m = len(M[0])
    result = [0] * m
    for j in range(m):
        for i in range(n):
            val = v[i] * M[i][j]
            if mod:
                val %= mod
                result[j] = (result[j] + val) % mod
            else:
                result[j] += val
    return result


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # Bottom-up DP + Math: O(m^3 * log(n)), O(m^2) space

        mod_factor = 10**9 + 7
        m = r - l + 1
        t = m * 2
        mat = [[0] * t for _ in range(t)]
        for i in range(m):
            for j in range(i + 1, m):
                mat[i][m + j] = 1
            for j in reversed(range(i)):
                mat[m + i][j] = 1
        mat = matpow(mat, n - 1, mod_factor)
        valid_zigzag_arrays = sum(vecmul([1] * t, mat, mod_factor)) % mod_factor
        return valid_zigzag_arrays
