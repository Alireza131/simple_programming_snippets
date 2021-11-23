class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        output = ''
        while curr:
            output += str(curr.value)
            curr = curr.next
        return output


def list2LinkedList(nums):
    head = None
    curr = None
    for n in nums:
        if not head:
            head = Node(n)
            curr = head
        else:
            curr.next = Node(n)
            curr = curr.next
    return head


n = Node(1, Node(2, Node(3)))


print(list([10, 20, 30]))