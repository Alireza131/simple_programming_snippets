
class Node(object):
    def __init__(self,value=None,Next=None):
        self.value=value
        self.next=Next

class Solution:
    def add2Nums(self, l1, l2,c):
        val = l1.value+ l2.value+c
        c=val//10
        ret= Node(val%10)
        print(l1.value,l2.value,c,ret.value)
        if l1.next != None or l2.next != None:
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            ret.next=self.add2Nums(l1.next, l2.next,c)
        elif c:
            ret.next=Node(c)
        return ret

    def add2NumsIterative(self,l1,l2):
        a = l1
        b = l2
        c = 0
        ret=current = None
        while a or b:
            val = a.value + b.value + c
            c = val//10
            if not ret:
                ret = current=Node(val%10)

            else:
                ret.next=Node(val%10)

                ret=ret.next
            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            elif c:
                ret.next = Node(c)
            a=a.next
            b=b.next
        return current

#245 as a linked list 2->4->5
l1=Node(2)
l1.next = Node(4)
l1.next.next = Node(3)
#564
l2=Node(5)
l2.next= Node(6)
l2.next.next= Node(4)

s= Solution().add2NumsIterative(l1,l2)
print(s.value,s.next.value,s.next.next.value)


