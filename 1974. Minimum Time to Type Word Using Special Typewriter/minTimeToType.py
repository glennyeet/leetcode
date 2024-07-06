class Solution:
    def minTimeToType(self, word: str) -> int:
        # alphabet = list(map(chr, range(97, 123)))
        # pointerPosition = 0
        # seconds = 0
        # for c in word:
        #     cPosition = alphabet.index(c)
        #     if pointerPosition < cPosition:
        #         forwards = cPosition - pointerPosition
        #         backwards = pointerPosition - 0 + 26 - cPosition
        #         seconds += min(forwards, backwards)
        #     elif pointerPosition > cPosition:
        #         backwards = pointerPosition - cPosition
        #         forwards = 26 - pointerPosition + cPosition - 0
        #         seconds += min(forwards, backwards)
        #     pointerPosition = cPosition
        #     seconds += 1
        # return seconds
        pointerPosition = ord('a')
        seconds = 0
        for c in word:
            cPosition = ord(c)
            distance = abs(pointerPosition - cPosition)
            seconds += min(distance, 26 - distance) + 1
            pointerPosition = cPosition
        return seconds
    