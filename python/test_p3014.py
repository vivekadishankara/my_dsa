class Solution:
    def minimumPushes1(self, word: str) -> int:
        n = len(word)

        division = n // 8
        modulo = n % 8

        key_push = 0

        for multiplier in range(division):
            key_push += 8 * (multiplier + 1)

        key_push += modulo * (division + 1)

        return key_push

    def minimumPushes(self, word: str) -> int:
        n = len(word)

        division = n // 8

        key_push = 0

        for multiplier in range(division):
            key_push += 8 * (multiplier + 1)

        key_push += (n % 8) * (division + 1)

        return key_push