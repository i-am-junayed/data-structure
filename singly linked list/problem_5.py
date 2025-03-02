# Remove the even numbers from the following singly linked list. Write a utility function
# deleteeven(self) that will delete all even nodes from the singly linedlist

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


  def delete_even_nodes(self):
      while self.head.data % 2 == 0:
          self.head = self.head.next
      
      current_node = self.head
      while(current_node.next != None):
          if current_node.next.data % 2 == 0:
              current_node.next = current_node.next.next
                  
          current_node = current_node.next



s = SinglyLinkedList()
s.append(4)
s.append(6)
s.append(7)
s.append(8)
s.append(9)
s.append(2)
s.append(9)
s.print_list()

s.delete_even_nodes()
s.print_list()
