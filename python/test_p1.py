from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, a_num in enumerate(nums):
            if nums_dict.get(target - a_num) is not None:
                return [nums_dict.get(target - a_num), i]
            else:
                nums_dict[nums[i]] = i
        return [0, 0]



@pytest.mark.parametrize("nums,target,answer", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def test_solution(nums, target, answer):
    assert Solution().twoSum(nums, target) == answer
