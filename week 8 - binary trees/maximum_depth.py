# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        deepest = 0
        def traverse(node, depth):
            nonlocal deepest

            if node.left:
                traverse(node.left, depth + 1)
            if node.right:
                traverse(node.right, depth + 1)
            
            deepest = max(deepest, depth)
        
        traverse(root, 1)

        return deepest