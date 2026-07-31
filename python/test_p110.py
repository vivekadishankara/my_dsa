from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode]) -> Tuple[bool, int]:
        if node is None:
            return True, 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        balanced = (left[0] and right[0]) and abs(left[1] - right[1]) < 2

        return balanced, 1 + max(left[1], right[1])

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
