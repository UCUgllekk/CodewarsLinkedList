class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"Node({self.data}, {self.next})"
def reverse(head):
    if not head:
        return head
    data = []
    new_head = head
    while new_head:
        data.append(new_head.data)
        new_head = new_head.next
    data = data[::-1]
    new_head = head
    for i in data:
        new_head.data = i
        new_head = new_head.next
    return head

# head = Node(1, Node(2, Node(3)))
# print(reverse(head))