### QUESTION : Write findMaxR(self, root) that will return the maximum of a BST using recursion. 

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


  # Find the node with the maximum value
  def find_max2(self):
    current = self.root
    while current.right_child:
        current = current.right_child
    return current.data
    
  # Find the node with the maximum value using recursion. So basically only this function is the answer of this question. 
  def find_maxR(self, root):
    if root == None:
      return

    if root.right_child == None:
      return root.data
    else:
      return  self.find_maxR(root.right_child)


num = [7, 15, 9, 8, 10, 5, 3, 16, 11, 13,  17]
for i in range (0,len(num)):

      bst.insert( num[i])

print("Inorder with recursion:")
bst.inorder(bst.root)
print()

bst.find_maxR(bst.root)


