# Write a function getAverage() that will take head of a singly linked list and return the average.
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

  def getAverage(self):
    sum = 0
    count = 0
    current_node = self.head
    while current_node != None:
      sum = sum + current_node.data
      count = count + 1
      current_node = current_node.next
    
    avg = sum / count
    return avg

s = SinglyLinkedList()
s.append(5)
s.append(9)
s.append(7)
s.append(5)
s.append(9)
s.append(2)
s.append(9)
s.print_list()
print(f"The average of this linked list is : {round(s.getAverage(),2)}")
