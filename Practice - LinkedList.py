# Some Pracices with Linked Lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    current_node = self.head
    if current_node is None:
        self.head = Node(value)
        return
    while current_node.next:
        current_node = current_node.next
    current_node.next = Node(value)

LinkedList.append = append

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    currend_node = self.head
    while currend_node.next:
        if currend_node.value == value:
            return currend_node
        currend_node = currend_node.next
    return None

LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    current_node = self.head
    if current_node.value == value:
        self.head = current_node.next
        return
    while current_node.next:
        if current_node.next.value == value:
            current_node.next = current_node.next.next
            return
        current_node = current_node.next

LinkedList.remove = remove

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    current_node = self.head
    value = current_node.value
    self.head = current_node.next
    return value

LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

