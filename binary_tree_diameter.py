'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self,node): 
        if node is None: 
            return 0 ;  

        else : 

            # Compute the depth of each subtree 
            lDepth = self.maxDepth(node.left) 
            rDepth = self.maxDepth(node.right) 

            # Use the larger one 
            if (lDepth > rDepth): 
                return lDepth+1
            else: 
                return rDepth+1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        Ldiameter = self.diameterOfBinaryTree(root.left)
        Rdiameter = self.diameterOfBinaryTree(root.right)
        
        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)
        return max((lDepth+rDepth),max(Ldiameter,Rdiameter))
        
        