class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = ListNode(data)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print()

    def addNodeAfterValue(self, givenValue, newValue):
        new_node = ListNode(newValue)
        current = self.head

        while current is not None:
            if current.data == givenValue:
                new_node.next = current.next
                new_node.prev = current

                if current.next is not None:  # If not last node, update next node's prev
                    current.next.prev = new_node
                else:
                    self.tail = new_node  # Update tail if inserting at the end

                current.next = new_node  # Always update current node's next
                return True  # Successfully inserted

            current = current.next  # Move to next node

        return False  # Value not found (Moved outside the while loop)

# Create and populate the linked list
dll = DoublyLinkedList()
dll.append(5)
dll.append(21)
dll.append(3)
dll.append(7)
dll.append(4)
dll.append(9)
dll.append(2)
dll.append(12)


dll.print_all() 
if not dll.addNodeAfterValue(2, 8):
    print("Value Not Found")

dll.print_all()
