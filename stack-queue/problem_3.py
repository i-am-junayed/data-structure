class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList: #Singly linkedlist Class (That we have learned earlier)
  def __init__(self):
    self.head = None
    #self.size = 0

# print the linked list
  def print_all(self):
    current_node = self.head
    while current_node != None:
      print(current_node.data, end =  "->")
      current_node = current_node.next
    print()

# Append data before the head of the list
  def append_left(self, new_data): #complexity  O(1)
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
    else:
      tmp = self.head
      self.head = new_node
      new_node.next = tmp

    #self.size += 1

# Delete data from  the head of the list
  def pop_left(self): #complexity  O(1)
    if self.head==None:
      print("List is empty")
    else:
      #self.size -= 1
      self.head = self.head.next

#implementing stack using the above Singly Linked List class
class Stack:
    def __init__(self):
        self.s = SinglyLinkedList()

    # def size(self): #Complexity O(1)
    #     return (self.s.size)

    def isempty(self): #Complexity O(1)
      if self.s.head == None:
        return True
      else:
        return False

    # Push data to the top of the stack
    def push(self, data): #Complexity O(1)
        self.s.append_left(data)

    def pop(self):
         self.s.pop_left()

    def peek(self):       #Complexity O(1)
      if self.s.head == None:
        print("Stack is empty")
      else:
        return self.s.head.data


#Optional/Extra function. Just only for display. No use for stack functionality
    def printStack(self): #complexity O(n)
       if self.isempty():
        print("Stack is empty")
       else:
        self.s.print_all()


# write a function to keep the largest value on top of the stack
def keepLargestOnTop(st):
  max = st.peek()
  helpSt = Stack()
  while(st.isempty() != True):
    val = st.peek()
    st.pop()
    helpSt.push(val)
    if (val > max):
      max = val


  while (helpSt.isempty() != True):
    val = helpSt.peek()
    if val != max:
      s.push(val)
    helpSt.pop()

  s.push(max)

#drive code
s.printStack()
keepLargestOnTop(s)
s.printStack()
