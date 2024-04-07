'''Convert a linked list to a string'''
class Node():
    '''Node'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node: "Node"):
    '''Returns linked list
    >>> stringify(Node(0, Node(1, Node(2, Node(3)))))
    '0 -> 1 -> 2 -> 3 -> None'
    >>> stringify(None)
    'None'
    '''
    output = []
    if isinstance(node, Node):
        while True:
            output.append(str(node.data))
            if node.next is not None:
                node = node.next
            else:
                output.append(str(node.next))
                break
        return " -> ".join(output)
    return "None"

# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())
