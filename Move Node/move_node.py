'''move node'''
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.data}, {self.next})"

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''Moves node from source to dest
    >>> source = Node(1, Node(2, Node(3)))
    >>> dest = Node(4, Node(5, Node(6)))
    >>> move_node(source, dest).source == 2 -> 3 -> None
    >>> move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> None
    '''
    if not source:
        raise ValueError
    new_dest = Node(source.data)
    new_dest.next = dest
    new_source = Node(source.next.data)
    new_source.next = source.next.next
    return Context(new_source, new_dest)

    # Alternative solution
    # if not source:
    #     raise ValueError
    # new_dest = Node(source.data)
    # new_dest.next = dest
    # new_source = source.next
    # return Context(new_source, new_dest)

# if __name__ == '__main__':
#     source = Node(1, Node(2, Node(3)))
#     dest = Node(4, Node(5, Node(6)))
#     move_node(source, dest)
