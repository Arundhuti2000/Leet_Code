# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self, root: Optional[TreeNode]):
        if root is None:
            return None
        self.mirror(root.left)
        self.mirror(root.right)
        temp = root.left
        root.left=root.right
        root.right=temp
        return root
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.mirror(root)
        return root