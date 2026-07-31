from collections import Counter

class Solution:
    def minimumPushes1(self, word: str) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        freq = sorted(freq, reverse=True)
        answer = 0
        for i, f in enumerate(freq):
            if f:
                multiplier = i // 8 + 1
                answer += f * multiplier

        return answer

    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)

        answer = 0
        for i, f in enumerate(freq):
            if f:
                multiplier = i // 8 + 1
                answer += f * multiplier

        return answer