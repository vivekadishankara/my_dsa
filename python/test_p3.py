from typing import Optional

import pytest

class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        letters = dict()
        long = 0
        start = 0
        end = 0
        for pos, a_letter in enumerate(s):
            early_pos = letters.get(a_letter) 
            if early_pos is not None:
                start = max(start, early_pos + 1)
            end += 1
            long = max(end - start, long)
            letters[a_letter] = pos

        return long

    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = dict()
        long = 0
        start = 0
        for pos, a_letter in enumerate(s):
            early_pos: Optional[int] = letters.get(a_letter)
            if early_pos is not None:
                start = max(start, early_pos + 1)
            long = max(pos - start + 1, long)
            letters[a_letter] = pos

        return long


@pytest.mark.parametrize("string, answer",
    [
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["pwwkew", 3],
        ["abcd", 4],
        ["aab", 2],
        ["abba", 2],
    ]
)
def test_solution(string, answer):
    assert Solution().lengthOfLongestSubstring(string) == answer