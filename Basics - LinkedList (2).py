# Additional methonds for the Linked List class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Adds the element at the end of list
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    # Converts the Linked List to Python list
    def to_list(self):
        out = []
        
        if self.head is None:
            return out
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

### TEST CODE ###
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")