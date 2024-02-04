# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def findMaxDepth(self, root : Optional[TreeNode], diameter : List[int]) -> int:
        
        
        if not root:
            return 0
        
        left_ht = self.findMaxDepth(root.left, diameter)
        right_ht = self.findMaxDepth(root.right, diameter)
        diameter[0] = max(diameter[0], left_ht+right_ht)
        return 1+max(left_ht,right_ht)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [-1]
        _ = self.findMaxDepth(root, diameter) 
        
        return diameter[0]
        
        
        
        
        