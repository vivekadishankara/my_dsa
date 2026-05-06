from typing import List

import pytest

INT_MIN = -10**6
INT_MAX = 10**6

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid = (m + n + 1) // 2

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        min1 = 0
        max1 = m
        while min1 <= max1:
            m1 = (min1 + max1) // 2

            l1 = nums1[m1 - 1] if 0 < m1 <= m else INT_MIN
            l2 = nums2[mid - m1 - 1] if 0 < mid - m1 <= n else INT_MIN

            r1 = nums1[m1] if 0 <= m1 < m else INT_MAX
            r2 = nums2[mid - m1] if 0 <= mid - m1 < n else INT_MAX

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return float(max(l1, l2))

            if l1 > r2:
                max1 = m1 - 1
            else:
                min1 = m1 + 1
        return 0.0


@pytest.mark.parametrize(
    'nums1, nums2, answer',
    [
        ([1, 2, 6, 15], [4, 7, 16], 6.0),
        ([1,3], [2], 2.00000),
        ([1,2], [3,4], 2.50000),
        ([],[1], 1.0),
        ([1], [], 1.0),
        ([1,2,3], [4,5,6], 3.5),
        ([1,2,3], [4,5,6,7], 4.0),
        ([1,2,3], [1,2,3], 2.0),
    ]
)
def test_solution(nums1, nums2, answer):
    assert Solution().findMedianSortedArrays(nums1, nums2) == answer