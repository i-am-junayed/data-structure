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
    if  self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node

  def print_all(self):
    current_node = self.head
    while current_node:
      print(current_node.data, end =" <-> ")
      current_node = current_node.next
    print()

  
  def delete_3rd_element_from_last(self):
    current = self.tail
    for i in range(2):
      current = current.prev
    
    current.prev.next = current.next
    current.next.prev = current.prev

dll = DoublyLinkedList()
dll.append(5)
dll.append(2)
dll.append(3)
dll.append(7)
dll.append(4)
dll.append(9)
dll.append(2)
dll.append(6)

dll.print_all()
dll.delete_3rd_element_from_last()
dll.print_all()
