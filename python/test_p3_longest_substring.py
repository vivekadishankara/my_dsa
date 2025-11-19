import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        char_dict = {}
        len_sub_string = 0

        for i, c in enumerate(s):
            if char_dict.get(c) is not None:
                repeat = char_dict[c]
                if repeat >= start:
                    start = repeat + 1
            char_dict[c] = i
            len_sub_string = max(len_sub_string, i - start + 1)
        return len_sub_string

@pytest.mark.parametrize("s, answer", [
    ["abcabcbb", 3],
    ["bbbbb", 1],
    ["pwwkew", 3],
    [" ", 1],
    ["dvdf", 3],
    ["au", 2],
    ["cdd", 2],
    ["bbtablud", 6],
    ["aabaab!bb", 3]
])
def test_longest_substring(s, answer):
    assert Solution().lengthOfLongestSubstring(s) == answer
