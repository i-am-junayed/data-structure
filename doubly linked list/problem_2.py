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


  def append_left(self, data):
    newnode = ListNode(data)
    if self.head == None:
      self.head = newnode
      self.tail = newnode
    else:
      newnode.next = self.head
      self.head.prev = newnode
      self.head = newnode
    self.size +=1

  def print_all(self):
    current_node = self.head
    while current_node:
      print(current_node.data, end =" <-> ")
      current_node = current_node.next
    print()


  def isSymmetric(self):
    right = self.head
    left = self.tail

    while( right and left is not None):
      if right.data != left.data:
        return False
      else:
        right = right.next
        left = left.prev
      
    if right is not None or left is not None:
      return False
    else:
      return True 


dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(1)

dll.print_all()
print(dll.isSymmetric()) 

dll_2 = DoublyLinkedList()
dll_2.append(1)
dll_2.append(2)
dll_2.append(4)
dll_2.append(3)
dll_2.append(1)

dll_2.print_all()
print(dll_2.isSymmetric()) 
