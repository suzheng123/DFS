"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return
        
        
        upper = lower = root

        while root:
            if root and root.val > target:
                upper = root
                root = upper.left
            
            if root and root.val < target:
                lower = root
                root = lower.right
            
            if root and root.val == target:
                return root.val
        
        if abs(upper.val-target) < abs(lower.val- target):
            return upper.val
        
        return lower.val