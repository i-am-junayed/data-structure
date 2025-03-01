# Assume, Head is the head-node of a singly linked list (sll). 
# Write a utility function addNodeBeforeValue (self, givenValue, newValue) to insert a new value in this sll just before 
# the given value.
# If the given value is found in the sll, insert the new value just before the given value.
# If the given value is not found, don’t add the node. Just print “Not found”

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
    
  def addNodeBeforeValue(self, givenValue, newValue):
    if self.head.data == givenValue:
        new_node = Node(newValue)
        new_node.next = self.head
        self.head = new_node
    else:
        current_node = self.head
        while current_node.next != None:
            if current_node.next.data == givenValue:
                new_node = Node(newValue)
                new_node.next = current_node.next
                current_node.next = new_node
                self.print_list()
                return
            
            current_node = current_node.next
    
    print("Not Found")          
      
s = SinglyLinkedList()
s.append(4)
s.append(9)
s.append(7)
s.append(8)
s.append(9)
s.append(2)
s.append(9)
s.print_list()

s.addNodeBeforeValue(2, 7)
 
