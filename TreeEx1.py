class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    def _preorder_helper(self, n, ret):
        if not n:
            return
        ret += ' '+str(n.value)
        self._preorder_helper(n.left,ret)
        self._preorder_helper(n.right,ret)
    def _inorder_helper(self, n, ret):
        if not n:
            return
        self._inorder_helper(n.left, ret)
        ret += ' '+str(n.value)
        self._inorder_helper(n.right, ret)
    def _postorder_helper(self,n,ret):
        if not n:
            return
        self._postorder_helper(n.left, ret)
        self._postorder_helper(n.right, ret)
        ret += ' ' + str(n.value)

    def preorder(self, n):
        ret=[]
        self._preorder_helper(n,ret)
        return ''.join(ret)
    def inorder(self,n):
        ret=[]
        self._inorder_helper(n,ret)
        return ''.join(ret)
    def postorder(self,n):
        ret=[]
        self._postorder_helper(n,ret)
        return ''.join(ret)
n = Node(1,Node(3,Node(2),Node(5)),Node(4)) #this is the important part.
n2= Node(2,None,Node(3))
print(Solution().preorder(n2))
print(Solution().inorder(n))
print(Solution().postorder(n))
