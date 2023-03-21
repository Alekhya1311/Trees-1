# Time Complexity - O(n)
# Space Complexity - O(H), H is height of the tree



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.prev = None
        self.inorder(root)
        return self.flag

    def inorder(self,root):
        if root == None :
            return 
        
        if self.flag:
            self.inorder(root.left)
           
            if (self.prev != None  and self.prev.val >= root.val) :
                self.flag = False
        self.prev = root
        
        if self.flag:
           
            self.inorder(root.right)