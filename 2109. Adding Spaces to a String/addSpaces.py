class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sentence = []
        spaces_set = set(spaces)
        for i, c in enumerate(s):
            if i in spaces_set:
                sentence.append(" ")
            sentence.append(c)
        return "".join(sentence)
