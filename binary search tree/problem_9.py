# Find the sum of even numbers in each of the level. 

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a node with data into the BST
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

            if newnode.data < parent.data:
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


    def print_levels_wise_even_sum(self):
        if self.root is None:
            return

        queue = deque([self.root])

        level = 0
        while queue:
            level_size = len(queue)
            sum = 0

            for i in range(level_size):

                node = queue.popleft()
                if node.data % 2 == 0:
                  sum = sum + node.data

                if node.left_child:
                    queue.append(node.left_child)
                if node.right_child:
                    queue.append(node.right_child)
            print(f"Sum of even nodes at level: {level} is : {sum}")
            level = level + 1

bst = BinarySearchTree()

# Example tree:
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

num = [7, 15, 9, 8, 10, 5, 3, 16, 11, 13, 17]
for i in range(len(num)):
    bst.insert(num[i])

print("Inorder with recursion:")
bst.inorder(bst.root)
print("\nLevel-wise sum:")
bst.print_levels_wise_even_sum()
