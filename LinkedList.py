# Linked List Class:

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Head 2 -> 1 -> 4 -> 3 -> 5 -> None

head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

print("All values of the List")
print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)

# Now that as a function which iterates through the Linked List
def print_linked_list(head):
    out = "The Linked List: "
    current_node = head
    
    while current_node is not None:
        out += str(current_node.value) + " -> "
        current_node = current_node.next
    out += str(None)
    print(out)

print_linked_list(head)

