# Valid binary search tree such that left<node<right

class Node(object):
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left=left
        self.right=right
class Solution(object):
    def traverse(self, n, low, high):
        if not n:
            return True
        val = n.value
        if ((val>low and val<high)and self.traverse(n.left,low,n.value)and self.traverse(n.right,n.value,high)):
            return True
        return False
    def is_valid(self,n):
        return self.traverse(n,low=float('-inf'),high=float('inf'))

n= Node(5)
n.left= Node(4)
n.right=Node(6)
print(Solution().is_valid(n))

