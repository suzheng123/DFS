"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
       if not root:
           return
       
       rootSum = None
       minSum = None
       minRoot = root
       stack = [root]
       while stack:
           node = stack.pop()
           rootSum = self.subTreeSum(node)
           print 'node, rootSum: ', node.val, rootSum
           if minSum is None:
               minSum = rootSum
               
               
           if rootSum < minSum:
               minSum = rootSum
               minRoot = node
               print 'Therefore, minSum is: --------->  ',minSum, minRoot.val
               
               
           if node.left:
               stack.append(node.left)
           if node.right:
               stack.append(node.right)
       return minRoot
        
    def subTreeSum(self,root):
        if not root:
            return
        stack = [root]
        subSum = 0
        while stack:
            node = stack.pop()
            subSum += node.val
            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)
            if node.left and not node.right:
                stack.append(node.left)
            if not node.left and node.right:
                stack.append(node.right)
        return subSum