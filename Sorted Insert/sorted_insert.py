class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if not head:
        return Node(data)
    output = []
    while True:
        output.append(str(head.data))
        if head.next is not None:
            head = head.next
        else:
            output.append(str(head.next))
            break
    output.append(data)
    output = sorted(list(map(float, [i for i in output if i != 'None'])))[::-1]
    temp = None
    for i in range(len(output)):
        head = Node(float(output[i]))
        head.next = temp
        temp = head
    return head
    # Your code goes here.
    # Make sure to return the head of the list.
