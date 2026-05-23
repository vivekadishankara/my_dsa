import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        curr_long = 1
        pointer = 1
        while pointer < len(s):
            left = pointer - 1
            right = pointer + 1
            while left >= 0 and len(s) > right and s[left] == s[right]:
                sub = s[left : right + 1]
                if len(sub) > curr_long:
                    curr_long = len(sub)
                    longest = sub
                left -= 1
                right += 1

            left = pointer - 1
            right = pointer
            while left >= 0 and len(s) > right and s[left] == s[right]:
                sub = s[left: right + 1]
                if len(sub) > curr_long:
                    curr_long = len(sub)
                    longest = sub
                left -= 1
                right += 1
            pointer += 1

        return longest


@pytest.mark.parametrize(
    's, expected',
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("abcdcba", "abcdcba"),
        ("acb", "a"),
        ("abbcccba", "bcccb")
    ]
)
def test_solution(s, expected):
    assert Solution().longestPalindrome(s) == expected
