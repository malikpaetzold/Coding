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

# Creating a Linked List by iterating over input

def create_linked_list(input_list):
    head = None
    tail = None
    
    for value in input_list:
        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next
    
    return head

### TEST CODE ###
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
        
        

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)