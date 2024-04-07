'''Get nth node'''
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __str__(self) -> str:
        return f"Node({self.data}, {self.next})"

def get_nth(node, index):
    '''
    >>> linked_list = Node(1, Node(2, Node(3, None)))
    >>> get_nth(linked_list, 0).data
    1
    >>> get_nth(linked_list, 1).data
    2
    >>> get_nth(linked_list, 2).data
    3
    >>> get_nth(linked_list, 100)

    '''
    counter = 0
    while node is not None:
        if counter == index:
            break
        node = node.next
        counter += 1
    if counter != index or node is None:
        raise ValueError
    return node

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
