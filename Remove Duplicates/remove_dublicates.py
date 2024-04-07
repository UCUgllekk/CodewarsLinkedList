class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.data}, {self.next})"

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__

def remove_duplicates(head):
    '''removes dublicates from head
    >>> head1 = Node(1)
    >>> head3 = Node(1, Node(2, Node(2, Node(3, Node(4, Node(5, None))))))
    >>> remove_duplicates(head1) == head1
    True
    >>> remove_duplicates(head2) == Node(1, Node(2, None))
    True
    '''
    if not head or not head.next:
        return head
    nodes = set()
    while head:
        nodes.add(head.data)
        head = head.next
    nodes = list(map(int, nodes))[::-1]
    print(nodes)
    temp = None
    for _,v in enumerate(nodes):
        node = Node(int(v))
        node.next = temp
        temp = node
    return node

if __name__ == '__main__':
    head2 = Node(1, Node(2, Node(2)))
    head3 = Node(1, Node(2, Node(2, Node(3, Node(4, Node(5))))))
    remove_duplicates(head3)
    import doctest
    print(doctest.testmod())
