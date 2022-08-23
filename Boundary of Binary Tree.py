# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:54:23 2022

@author: Avinash Kumar
"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
def boundaryOfBinaryTree(root: TreeNode):
        if not root:
            return []
        boundary = [root.val]
        
        def dfsleft(node):
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)
            if node.left:
                dfsleft(node.left)
            else:
                dfsleft(node.right)
                
        def leaf(node):
            if not node:
                return
            
            leaf(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            leaf(node.right)
            
        def dfsright(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                dfsright(node.right)
            else:
                dfsright(node.left)
            boundary.append(node.val)
            
        dfsleft(root.left)
        leaf(root)
        dfsright(root.right)
        return boundary
    
node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6, TreeNode(9), TreeNode(10))))
res = boundaryOfBinaryTree(node)
print(res)