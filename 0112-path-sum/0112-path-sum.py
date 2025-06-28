# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasSum(self,root: Optional[TreeNode], targetSum: int, currentSum: int):
        currentSum+=root.val
        if (currentSum == targetSum and root.left is None and root.right is None):
            return True
        if root.left:
            if(self.hasSum(root.left, targetSum,currentSum)):
                return True
        if root.right:
            if(self.hasSum(root.right, targetSum,currentSum)):
                return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.hasSum(root, targetSum,0)
        