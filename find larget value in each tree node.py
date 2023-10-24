# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(node):
            q=[[node]]
            ans=[node.val]
            while len(q)>0:
                lst=q.pop(0)
                m=-2**31
                lst1=[]
                for i in lst:
                    if i.left:
                        lst1.append(i.left)
                        m=max(m,i.left.val)
                    if i.right:
                        lst1.append(i.right)
                        m=max(m,i.right.val)
                if len(lst1)>0:
                    q.append(lst1)
                    ans.append(m)
            return ans
        if root==None:
            return []
        return bfs(root)