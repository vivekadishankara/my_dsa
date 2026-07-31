class Solution:
    def smallestPalindrome1(self, s: str) -> str:
        mid = s[: len(s) // 2]
        mid = sorted(mid)
        j = len(mid) - 1
        if len(s) % 2 == 0:
            i = len(mid)
            mid += ["0"] * len(mid)
        else:
            i = len(mid) + 1
            mid += [s[len(s) // 2]] + ["0"] * len(mid)

        k = 0
        for ix in range(i, len(s)):
            mid[ix] = mid[j - k]
            k += 1

        return ''.join(mid)

    def smallestPalindrome(self, s: str) -> str:
        mid = s[:len(s) // 2]

        if len(s) % 2 == 0:
            return ''.join(sorted(mid) + sorted(mid, reverse=True))
        else:
            return ''.join(sorted(mid) + [s[len(s) // 2]] + sorted(mid, reverse=True))


print(Solution().smallestPalindrome("babab"))
print(Solution().smallestPalindrome("baab"))