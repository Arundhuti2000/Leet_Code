# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, t1:Optional[TreeNode], t2:Optional[TreeNode]):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        firstMirror= self.isMirror(t1.left,t2.right)
        secondMirror= self.isMirror(t1.right, t2.left)
        return t1.val==t2.val and firstMirror and secondMirror

    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)