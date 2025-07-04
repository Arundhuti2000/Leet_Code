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
        queue=deque([root])
        result=[]
        zigzag=False
        while len(queue)>0:
            curr_level_nodes=[]
            level_size=len(queue)
            for i in range(0, level_size):
                if zigzag:
                    node=queue.pop()
                    curr_level_nodes.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                else:
                    node=queue.popleft()
                    curr_level_nodes.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(curr_level_nodes)
            zigzag= not zigzag
        return result