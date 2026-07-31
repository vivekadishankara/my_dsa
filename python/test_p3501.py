import bisect
from typing import List


class Solution:
    def __init__(self):
        self.zsizes = list()
        self.starts = list()
        self.ends = list()
        self.pairsums = list()
        self.btree = list()

    def makeBtree(self):
        if self.pairsums:
            self.btree = [0] * 4 * len(self.pairsums)
            self.treedf(0, 0, len(self.pairsums) - 1)

    def treedf(self, i: int, il: int, ir: int):
        if il == ir:
            self.btree[i] = self.pairsums[ir]
            return

        mid = (ir + il) // 2
        left = 2 * i + 1
        right = 2 * i + 2
        self.treedf(left, il, mid)
        self.treedf(right, mid + 1, ir)

        self.btree[i] = max(self.btree[left], self.btree[right])

    def get_max_btree(self, low: int, high: int):
        return self.get_max_df(low, high, 0, 0, len(self.pairsums) - 1)

    def get_max_df(self, low: int, high: int, i: int, il: int, ir: int) -> int:
        if il >= low and ir <= high:
            return  self.btree[i]
        elif ir < low or il > high:
            return  0
        else:
            mid = (il + ir) // 2
            return max(self.get_max_df(low, high, 2 * i + 1, il, mid), self.get_max_df(low, high, 2 * i + 2, mid + 1, ir))

    def lower_bound(self, il: int):
        for i in range(len(self.ends)):
            if il <= self.ends[i]:
                return i
        return len(self.ends)

    def lower_bound_bin(self, il: int):
        lb = len(self.ends) - 1
        i, j = 0, lb

        while i <= j:
            mid = (i + j) // 2
            if self.ends[mid] >= il:
                lb = mid
                j = mid - 1
            else:
                i = mid + 1
        return lb

    def upper_bound(self, ir: int):
        for i in range(len(self.starts) - 1, -1, -1):
            if ir >= self.starts[i]:
                return i
        return 0

    def upper_bound_bin(self, ir: int):
        up = 0
        i, j = 0, len(self.starts) - 1
        while i <= j:
            mid = (i + j) // 2
            if ir >= self.starts[mid]:
                up = mid
                i = mid + 1
            else:
                j = mid - 1
        return up

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')
        answer = [ones] * len(queries)
        if ones == len(s):
            return answer
        i = 0
        last_size = -1
        while i < len(s):
            if s[i] == '0':
                conti = 0
                while i + conti < len(s) and s[i] == s[i + conti]:
                    conti += 1
                self.zsizes.append(conti)
                self.starts.append(i)
                i += conti
                self.ends.append(i - 1)

                if last_size != -1:
                    self.pairsums.append(conti + last_size)
                last_size = conti
            else:
                i += 1

        self.makeBtree()

        for i, (il, ir) in enumerate(queries):
            low = self.lower_bound_bin(il)
            high = self.upper_bound_bin(ir)

            if low >= high:
                continue

            size_l = self.ends[low] - max(il, self.starts[low]) + 1
            size_h = min(ir, self.ends[high]) - self.starts[high] + 1

            if high - low == 1:
                answer[i] += size_l + size_h
                continue

            pair_l = size_l + self.zsizes[low + 1]
            pair_h = self.zsizes[high - 1] + size_h

            max_mid = self.get_max_btree(low + 1, high - 2)

            answer[i] += max(pair_l, max_mid, pair_h)
        return answer



# #
# print(Solution().maxActiveSectionsAfterTrade("0100", [[0,3],[0,2],[1,3],[2,3]]))
# print(Solution().maxActiveSectionsAfterTrade("010", [[1,2],[1,1]]))
# print(Solution().maxActiveSectionsAfterTrade("01011", [[3,4]]))
# print(Solution().maxActiveSectionsAfterTrade("11010", [[0,1]]))
# print(Solution().maxActiveSectionsAfterTrade("101101", [[2, 3]]))
# print(Solution().maxActiveSectionsAfterTrade("1000100", [[1,5], [0,6], [0,4]]))
# print(Solution().maxActiveSectionsAfterTrade("0101110001101", [[0,7],[0,12]]))
# print(Solution().maxActiveSectionsAfterTrade("001000001001011", [[3,8],[3,6],[14,14],[1,12],[10,12]]))
# print(Solution().maxActiveSectionsAfterTrade("001000001001011", [[3,8],[3,6],[14,14],[1,12],[10,12]]) == [5,5,5,12,7])
# print(Solution().maxActiveSectionsAfterTrade("10001010010001001000101001000100", [[2,30], [0,31]]) == [15,15])