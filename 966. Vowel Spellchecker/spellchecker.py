from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Hash Table: O(ws + qt) time, O(w + q) space, where w is the size of
        # wordlist, s is the size of the largest string in wordlist, q, is the
        # size of queries, and t is the size of the largest string in queries

        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        case_sensitive_words = set(wordlist)

        def convert_to_consonant_filter(word: str):
            consonant_filter = []
            for char in word:
                if char in vowels:
                    consonant_filter.append("*")
                else:
                    consonant_filter.append(char)
            return "".join(consonant_filter).lower()

        case_insensitive_words = {}
        consonant_filters = {}
        for word in wordlist:
            lowercase_word = word.lower()
            if lowercase_word not in case_insensitive_words:
                case_insensitive_words[word.lower()] = word
            consonant_filter = convert_to_consonant_filter(word)
            if consonant_filter not in consonant_filters:
                consonant_filters[consonant_filter] = word
        answer = []
        for query in queries:
            lowercase_word = query.lower()
            consonant_filter = convert_to_consonant_filter(query)
            if query in case_sensitive_words:
                answer.append(query)
            elif lowercase_word in case_insensitive_words:
                answer.append(case_insensitive_words[lowercase_word])
            elif consonant_filter in consonant_filters:
                answer.append(consonant_filters[consonant_filter])
            else:
                answer.append("")
        return answer
