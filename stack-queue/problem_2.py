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

#Special singly linked list with head and tail

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class SpecialSinglyLinkedList: #Special Singly Linked List with head and tail
  def __init__(self):
    self.head = None
    self.tail = None
    # self.size = 0

  def print_all(self):
    current_node = self.head
    while current_node:
      print(current_node.data, end = " ")
      current_node = current_node.next
    print()
  # Append data to the end of the linked list. It is updating the tail
  def append(self, new_data):  #complexity  O(1)
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    # self.size += 1

  # Delete data from  the head of the list. It is using head
  def pop_left(self): #complexity  O(1)
    if self.head==None:
      print("List is empty")
    else:
      # self.size -= 1
      if (self.head == self.tail): #Only one element present inside the linked list. It is head and also it is tail
        self.head = None
        self.tail = None
      else:
        self.head = self.head.next

#implementing Queue using Special Singly Linked List with head and tail
class Queue:
    def __init__(self):
        self.q = SpecialSinglyLinkedList()

    # def size(self):
    #     return (self.q.size)

    def isempty(self): #O(1)
      if self.q.head == None:
        return True
      else:
        return False

    # Push data to the top of the queue
    def enqueue(self, data): #Complexity O(1)
        self.q.append(data)

    def dequeue(self):      #Complexity O(1)
         self.q.pop_left()

    def peek(self):         #Complexity O(1)
      if self.isempty():
        print("Stack is empty")
      else:
        return self.q.head.data


#Optional/Extra function. Just only for display. No use for queue functionality
    def printQueue(self):
       if self.isempty():
        print("Queue is empty")
       else:
        self.q.print_all()



def check_length(q):
  length = 0
  h_q = Queue()
  while not q.isempty():
    length +=1
    val = q.peek()
    h_q.enqueue(val)
    q.dequeue()

  return length, h_q

def check_balance(q):
  check_len, q = check_length(q)
  if check_len % 2 != 0:
    return False

  st = Stack()
  for i in range(check_len//2):
    val = q.peek()
    st.push(val)
    q.dequeue()

  for i in range(check_len//2):
    val_1 = st.peek()
    val_2 = q.peek()
    st.pop()
    q.dequeue()
    if (val_1 == "(" or val_1 == ")") and (val_2 == "(" or val_2 == ")"):
      if val_1 == val_2:
        return False
    elif (val_1 == "{" or val_1 == "}") and (val_2 == "{" or val_2 == "}"):
      if val_1 == val_2:
        return False
    elif (val_1 == "[" or val_1 == "]") and (val_2 == "[" or val_2 == "]"):
      if val_1 == val_2:
        return False
    else:
      return False

  return True


q = Queue()
val = 1
while val != "0":
  val = input("Enter a bracket or if you want to stop enter 0 : ")
  if val != "0":
    q.enqueue(val)

q.printQueue()
if check_balance(q):
  print("The String is Balanced")
else:
  print("The String is not Balanced")
