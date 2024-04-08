class Node(object):
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"Node({self.data}, {self.next})"

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f"Context({self.first},\n {self.second})"

def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    odd = Node(head.data)
    even = Node(head.next.data)
    copy_odd = odd
    copy_even = even
    counter = 1
    while head:
        if counter%2:
            while copy_odd.next:
                copy_odd = copy_odd.next
            copy_odd.next = Node(head.data)
        else:
            while copy_even.next:
                copy_even = copy_even.next
            copy_even.next = Node(head.data)
        head = head.next
        counter += 1
    odd = odd.next
    even = even.next
    return Context(odd, even)
