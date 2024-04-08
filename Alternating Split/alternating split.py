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


def push(head, data):
  newNode = Node(data)
  newNode.next = head
  return newNode

def build_one_two_three():
  head = None
  head = push(head, 3)
  head = push(head, 2)
  head = push(head, 1)
  return head
  
def build_one_two():
  head = None
  head = push(head, 2)
  head = push(head, 1)
  return head

def build_one_two_three_four_five_six():
  head = None
  head = push(head, 6)
  head = push(head, 5)
  head = push(head, 4)
  head = push(head, 3)
  head = push(head, 2)
  head = push(head, 1)
  return head
  
def build_list(data):
  data.reverse()
  head = None
  for num in data:
    head = push(head, num)
  return head

print(alternating_split(build_list([5, 6, 1, 2, 3, 3, 3, 4, 8, 5, 4, 1])))
head = Node(1, Node(2))
head = Node(1, Node(2))
# print(alternating_split(head))