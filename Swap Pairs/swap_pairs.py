class Node:
    def __init__(self,data= None, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.data}, {self.next})"
    def __repr__(self) -> str:
        return f"Node({self.data}, {self.next})"

def swap_pairs(head):
    if not head:
        return head
    current_node = head
    new_head = head.next
    while current_node and current_node.next:
        temp = current_node.next
        current_node.next = current_node.next.next
        temp.next,current_node = current_node, temp.next
        if current_node and current_node.next:
            temp.next.next = current_node.next
    return new_head