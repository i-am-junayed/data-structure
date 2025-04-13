### QUESTION : Write a function named print_levels(self) that will print the height of a BST. 

class Node:
  def __init__(self, data):
    self.data = data
    self.left_child = None
    self.right_child = None

class BinarySearchTree:
  def __init__(self):
    self.root = None


  #Insert a node with data into the BST
  def insert(self, data):
    newnode = Node(data)
    if self.root is None:
      self.root = newnode
    else:
      current = self.root
      parent = None
      while current:
        parent = current
        if newnode.data < current.data:
          current = current.left_child
        else:
          current = current.right_child

      if  newnode.data < parent.data:
          parent.left_child = newnode
      else:
          parent.right_child = newnode


  def inorder(self, node):
    if node is None:
      return
    else:
      self.inorder(node.left_child)
      print(node.data, end = ", ")
      self.inorder(node.right_child)

  def preorder(self, node):
    if node is None:
      return
    else:
      print(node.data, end = ", ")
      self.preorder(node.left_child)
      self.preorder(node.right_child)

  def postorder(self, node):
    if node is None:
      return
    else:
      self.postorder(node.left_child)
      self.postorder(node.right_child)
      print(node.data, end = ", ")
      
  def print_levels(self):
    if self.root is None:
      return
          
    current_level = [self.root]
    while current_level:
      next_level = []
      for node in current_level:
        print(node.data, end=" ")
        if node.left_child:
          next_level.append(node.left_child)
        if node.right_child:
          next_level.append(node.right_child)
      print()  # Move to the next line for the next level
      current_level = next_level


bst = BinarySearchTree()

#                      7
#                    /  \
#                   5    15
#                  /     / \
#                 3     9   16
#                      / \   \
#                     8  10   17
#                           \
#                            11
#                              \
#                               13

num = [7, 15, 9, 8, 10, 5, 3, 16, 11, 13,  17]
for i in range (0,len(num)):

      bst.insert( num[i])

print("Inorder with recursion:")
bst.inorder(bst.root)
print("\nLevel wise printing : ")
bst.print_levels()
