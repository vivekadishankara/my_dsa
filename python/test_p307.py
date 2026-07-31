from typing import List


class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.btree = [0] * (4 * len(nums))
        self.formbtree(0, 0, len(nums) - 1)
        # self.print()

    def print(self):
        print(self.btree)

    def formbtree(self, i: int, left: int, right: int):
        if left == right:
            # print(i, left, "form")
            # self.print()
            self.btree[i] = self.nums[left]
            return

        mid = (left + right) // 2
        self.formbtree(2 * i + 1, left, mid)
        self.formbtree(2 * i + 2, mid + 1, right)

        self.btree[i] = self.btree[2 * i + 1] + self.btree[2 * i + 2]

    def updatetree(self, index: int, val: int, i: int, left: int, right):
        if left == right:
            self.btree[i] = val
            return

        mid = (left + right) // 2
        if index <= mid:
            self.updatetree(index, val, 2 * i + 1, left, mid)
        else:
            self.updatetree(index, val, 2 * i + 2, mid + 1, right)

        self.btree[i] = self.btree[2 * i + 1] + self.btree[2 * i + 2]

    def sumtree(self, left: int, right: int, i: int, il: int, ir: int) -> int:
        if right < il or left > ir:
            return 0
        elif left <= il and right >= ir:
            # print(il, ir)
            return self.btree[i]
        else:
            mid = (il + ir) // 2
            return self.sumtree(left, right, 2 * i + 1, il, mid) + \
                self.sumtree(left, right, 2 * i + 2, mid + 1, ir)

    def update(self, index: int, val: int) -> None:
        self.updatetree(index, val, 0, 0, len(self.nums) - 1)
        # self.print()

    def sumRange(self, left: int, right: int) -> int:
        return self.sumtree(left, right, 0, 0, len(self.nums) - 1)


class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.btree = [0] * (4 * len(nums))
        self.formbtree(0, 0, len(nums) - 1)

        self.index = 0
        self.val = 0

        self.left = 0
        self.right = 0

    def print(self):
        print(self.btree)

    def formbtree(self, i: int, left: int, right: int):
        if left == right:
            self.btree[i] = self.nums[left]
            return

        mid = (left + right) // 2
        self.formbtree(2 * i + 1, left, mid)
        self.formbtree(2 * i + 2, mid + 1, right)

        self.btree[i] = self.btree[2 * i + 1] + self.btree[2 * i + 2]

    def updatetree(self, i: int, left: int, right):
        if left == right:
            self.btree[i] = self.val
            return

        mid = (left + right) // 2
        if self.index <= mid:
            self.updatetree(2 * i + 1, left, mid)
        else:
            self.updatetree(2 * i + 2, mid + 1, right)

        self.btree[i] = self.btree[2 * i + 1] + self.btree[2 * i + 2]

    def sumtree(self, i: int, il: int, ir: int) -> int:
        if self.right < il or self.left > ir:
            return 0
        elif self.left <= il and self.right >= ir:
            return self.btree[i]
        else:
            mid = (il + ir) // 2
            return self.sumtree(2 * i + 1, il, mid) + self.sumtree(2 * i + 2, mid + 1, ir)

    def update(self, index: int, val: int) -> None:
        self.index = index
        self.val = val
        self.updatetree(0, 0, len(self.nums) - 1)

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        return self.sumtree(0, 0, len(self.nums) - 1)


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.btree = [0] * (4 * len(nums))
        self.formbtree(0, 0, len(nums) - 1)

        self.index = 0
        self.val = 0

        self.left = 0
        self.right = 0

    def print(self):
        print(self.btree)

    def formbtree(self, i: int, left: int, right: int):
        if left == right:
            self.btree[i] = self.nums[left]
            return

        mid = (left + right) // 2
        self.formbtree(2 * i + 1, left, mid)
        self.formbtree(2 * i + 2, mid + 1, right)

        self.btree[i] = self.btree[2 * i + 1] + self.btree[2 * i + 2]

    def updatetree(self, i: int, left: int, right):
        if left == right:
            self.btree[i] = self.val
            return

        mid = (left + right) // 2
        if self.index <= mid:
            self.updatetree(2 * i + 1, left, mid)
        else:
            self.updatetree(2 * i + 2, mid + 1, right)

        self.btree[i] += self.val - self.nums[self.index]

    def sumtree(self, i: int, il: int, ir: int) -> int:
        if self.right < il or self.left > ir:
            return 0
        elif self.left <= il and self.right >= ir:
            return self.btree[i]
        else:
            mid = (il + ir) // 2
            return self.sumtree(2 * i + 1, il, mid) + self.sumtree(2 * i + 2, mid + 1, ir)

    def update(self, index: int, val: int) -> None:
        self.index = index
        self.val = val
        self.updatetree(0, 0, len(self.nums) - 1)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        return self.sumtree(0, 0, len(self.nums) - 1)
    