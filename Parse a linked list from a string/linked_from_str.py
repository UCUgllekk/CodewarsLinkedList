'''Make listed linked list from string'''
class Node():
    '''Node'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.data}, {self.next})"

def linked_list_from_string(s:str | None):
    '''
    >>> head = Node(1, Node(2, Node(3)))
    >>> linked_list_from_string("1 -> 2 -> 3 -> None") == head
    True
    '''
    if s == 'None':
        return
    lst = s.split(' -> ')[::-1][1:]
    temp = None
    for i in range(len(lst)):
        node = Node(float(lst[i]), temp)
        temp = node
    return node

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())
