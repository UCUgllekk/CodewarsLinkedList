'''Get nth node'''
class Node(object):
    """Node class for reference"""
    def __init__(self):
        self.next = None

    def __str__(self) -> str:
        return f"Node({self.next})"

def loop_size(node):
    fast, slow = node, node
    length = 0
    start = 0
    while fast and slow:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            start += 1
            if start != 1:
                return length
        if start:
            length+=1
    return

# node1 = Node()
# node2 = Node()
# node3 = Node()
# node4 = Node()
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2
# print(loop_size(node1))