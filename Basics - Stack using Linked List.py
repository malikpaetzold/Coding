# Implement a stack using a linked list

# Add the Node class here
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # TODO: Add the __init__ method
    def __init__(self):
        self.head = None
        self.num_elements = 0
    
    # TODO: Add the push method
    def push(self, value):
        new_node = Node(value)
        # in case the stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.num_elements += 1
    
    # TODO: Add the pop method
    def pop(self):
        if self.num_elements == 0: return None
        out = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return out
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

# --- TEST ---
# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print ("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print ("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print ("Pass" if (stack.pop() == 60) else "Fail")
print ("Pass" if (stack.pop() == 40) else "Fail")
print ("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print ("Pass" if (stack.size() == 3) else "Fail")