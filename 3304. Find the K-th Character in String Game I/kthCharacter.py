class Solution:
    def kthCharacter(self, k: int) -> str:
        # Brute Force: O((log(k))^2) time, O(k) space

        word = ["a"]
        while True:
            if len(word) >= k:
                return word[k - 1]
            prev_len = len(word)
            for i in range(prev_len):
                if word[i] == "z":
                    word.append("a")
                else:
                    word.append(chr(ord(word[i]) + 1))
