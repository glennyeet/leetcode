class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Enumeration: O(n^2) time, O(n) space

        if numFriends == 1:
            return word
        n = len(word)
        largest_string = ""
        substring_len = n - numFriends + 1
        for i in range(n):
            substring = word[i : i + substring_len]
            if substring > largest_string:
                largest_string = substring
        return largest_string
