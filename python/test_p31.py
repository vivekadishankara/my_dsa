from typing import List


class Solution:
    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        gola_index = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                gola_index = i - 1
                break

        if gola_index != -1:
            swap_index = gola_index

            for i in range(n - 1, gola_index, -1):
                if nums[i] > nums[gola_index]:
                    swap_index = i
                    break

            nums[gola_index], nums[swap_index] = nums[swap_index], nums[gola_index]

        i = gola_index + 1
        j = n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        print(a)

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        gola_index = -1
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                gola_index = i - 1
                break

        if gola_index != -1:
            for i in range(n - 1, gola_index, -1):
                if nums[i] > nums[gola_index]:
                    nums[gola_index], nums[i] = nums[i], nums[gola_index]
                    break

        i = gola_index + 1
        j = n - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        print(a)
a = [1, 2, 3, 4]
sol = Solution()
sol.nextPermutation(a)
sol.nextPermutation(a)
sol.nextPermutation(a)
sol.nextPermutation(a)
sol.nextPermutation(a)
sol.nextPermutation(a)
sol.nextPermutation(a)
sol.nextPermutation(a)
