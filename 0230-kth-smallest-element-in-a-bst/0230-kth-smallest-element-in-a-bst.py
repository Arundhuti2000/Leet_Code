# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root:Optional[TreeNode], arr:list):
        if root is None:
            return None
        arr.append(root.val)
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr=[]
        self.preOrder(root,arr)
        arr.sort()
        return arr[k-1]