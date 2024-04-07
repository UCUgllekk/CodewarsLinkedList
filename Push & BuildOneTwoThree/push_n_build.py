'''Push N Build'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"Node({self.data}, {self.next})"

def push(head, data):
    '''
    >>> push(None, 1).data
    1
    >>> push(None, 1).next

    >>> push(Node(1), 2).data
    2
    >>> push(Node(1), 2).next.data
    1
    '''
    if head:
        new_node = Node(data)
        new_node.next = head
        return new_node
    return Node(data)

def build_one_two_three():
    '''Build a linked list
    >>> build_one_two_three().data
    1
    >>> build_one_two_three().next.data
    2
    >>> build_one_two_three().next.next.data
    3
    >>> build_one_two_three().next.next.next

    '''
    temp = None
    for i in range(3, 0, -1):
        node = Node(i)
        node.next = temp
        temp = node
    return node

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
