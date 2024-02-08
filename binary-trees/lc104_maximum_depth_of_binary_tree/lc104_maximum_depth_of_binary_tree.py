from typing import Optional
from lib.binary_tree import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calDepth(root)

    def calDepth(self, root) -> int:
        if root == None:
            return 0
        lh = 1 + self.calDepth(root.left)
        rh = 1 + self.calDepth(root.right)
        max_height = max(lh, rh)
        return max_height
