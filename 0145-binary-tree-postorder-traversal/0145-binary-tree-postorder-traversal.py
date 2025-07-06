# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,node, result):
            if not node:
                return []
            if node.left:
                self.postorder(node.left,result)
            if node.right:
                self.postorder(node.right, result)
            result.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.postorder(root, result)
        return result