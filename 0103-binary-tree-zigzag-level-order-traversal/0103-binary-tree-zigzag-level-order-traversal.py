# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=[root]
        result=[]
        level_index=1
        while len(queue)>0:
            curr_level_nodes=[]
            level_size=len(queue)
            for i in range(0, level_size):
                node=queue.pop(0)
                curr_level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_index%2==0:
                curr_level_nodes.reverse()
                result.append(curr_level_nodes)
            else:
                result.append(curr_level_nodes)
            level_index+=1
        return result