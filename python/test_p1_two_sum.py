import pytest
from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i, n in enumerate(nums):
            anti_target = target - n
            if sum_dict.get(anti_target) is None:
                sum_dict[n] = i
            else:
                return sum_dict[anti_target], i


@pytest.mark.parametrize("nums, target, answer",[
    [[2,7,11,15], 9, [0,1]],
    [[3,2,4], 6, [1,2]],
    [[3,3], 6, [0,1]],
])
def test_two_sum(nums, target, answer):
    actual_answer = Solution().twoSum(nums, target)
    assert list(actual_answer) == answer
