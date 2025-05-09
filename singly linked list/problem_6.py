# Write a utility function function named sorted_insert(self, v)  
# that takes a parameter v  and inserts it into a singly linked list in ascending order.

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next != None:
        current_node = current_node.next
      current_node.next = new_node

  def print_list(self):
    current_node = self.head
    while current_node != None:
      if current_node.next != None:
        print(current_node.data, end=" => ")
      else:
        print(current_node.data, end="")
      current_node = current_node.next
    print("\n")
    
  def sorted_insert(self, value):
      new_node = Node(value)

      if self.head is None or self.head.data >= value:
        new_node.next = self.head
        self.head = new_node
        return

      current = self.head
      while current.next is not None and current.next.data < value:
          current = current.next

      new_node.next = current.next
      current.next = new_node          
      
s = SinglyLinkedList()

s.sorted_insert(5)
s.sorted_insert(2)
s.sorted_insert(1)
s.sorted_insert(6)
s.sorted_insert(9)
s.sorted_insert(7)
s.sorted_insert(3)

s.print_list()
 
