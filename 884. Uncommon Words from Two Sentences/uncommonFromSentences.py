# from collections import defaultdict


# class Solution:
#     def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
#         s1_dict = defaultdict(int)
#         s2_dict = defaultdict(int)
#         s1_words = s1.split()
#         s2_words = s2.split()
#         for word1 in s1_words:
#             s1_dict[word1] += 1
#         for word2 in s2_words:
#             s2_dict[word2] += 1
#         uncommon_words = []
#         for word1 in s1_words:
#             if s1_dict[word1] == 1 and not s2_dict[word1]:
#                 uncommon_words.append(word1)
#         for word2 in s2_words:
#             if s2_dict[word2] == 1 and not s1_dict[word2]:
#                 uncommon_words.append(word2)
#         return uncommon_words


from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counter = Counter(s1.split() + s2.split())
        uncommon_words = []
        for word in counter:
            if counter[word] == 1:
                uncommon_words.append(word)
        return uncommon_words
