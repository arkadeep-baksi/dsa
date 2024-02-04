from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getLevelorderTraversal(self, root : Optional[TreeNode], ds : List[int])->List[int]:
        
        if not root:
            return []
        queue = deque()
        queue.append((root,0))
        
        max_level = -1
        while(queue):
            
            
            node,level = queue.popleft()
            ds.append((node.val,level))
            max_level = max(level,max_level)
            
            left = node.left
            right = node.right
            if left:
                queue.append((left,level+1))
            if right:
                queue.append((right,level+1))
        
        ans = [[] for _ in range(max_level+1)]
        
        for val,level in ds:
            ans[level].append(val)

        return ans
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        return self.getLevelorderTraversal(root,[])
        