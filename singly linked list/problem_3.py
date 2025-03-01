# You’re given the pointer to the head nodes of two singly linked lists. Compare the
# data in the nodes of the linked lists to check if they are equal. The lists are equal only
# if they have the same number of nodes and corresponding nodes contain the same
# data.

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
    
  def equalNode(self, sll_2):
      current_1 = self.head
      current_2 = sll_2.head
      while(current_1 != None and current_2 != None):
          if current_1.data == current_2.data:
              current_1 = current_1.next
              current_2 = current_2.next
          else:
              return False
              
      if current_1 is None and current_2 is None:
          return True
      else:
          return False
      
s = SinglyLinkedList()
s_2 = SinglyLinkedList()
s.append(5)
s.append(2)
s.append(1)
s.append(6)
s.append(9)
s.append(7)
s.append(3)

s_2.append(5)
s_2.append(2)
s_2.append(1)
s_2.append(6)
s_2.append(9)
s_2.append(7)
s_2.append(3)

if s.equalNode(s_2):
    print("They are equal")
else:
    print("They are not equal")
