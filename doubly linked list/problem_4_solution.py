class ListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_all(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print()

    def insertSorted(self, value):
        new_node = ListNode(value)

        # Insert at the beginning
        if self.head is None or self.head.data >= value:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:  # If list was empty, update tail
                self.tail = new_node
            return

        # Insert in the moddle position
        current = self.head
        while current.next and current.next.data < value:
            current = current.next

        # Insert after current
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node

        # If inserted at the end, update tail
        if new_node.next:
            new_node.next.prev = new_node
        else:
            self.tail = new_node


dll = DoublyLinkedList()
dll.append(2)
dll.append(5)
dll.append(10)
dll.append(15)

print("Before insertion:")
dll.print_all()

dll.insertSorted(12)   
dll.insertSorted(1)    
dll.insertSorted(20)   

print("After insertion:")
dll.print_all()
