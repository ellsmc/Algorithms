class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    # creates parent-child relationship
    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    # removes parent-child relationship
    def remove_child(self, child_node):
        print("Remove " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

#######################################################################################
# Tree Traversal

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.value = key


# Inorder Algorithm:
# 1. Traverse L subtree
# 2. Visit root
# 3. Traverse R subtree

def traverseInorder(root):
    """
    Time Complexity: O(N)
    Space: without size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree. 
    """
    if root:
        # Recur L first
        traverseInorder(root.left)
        # Print node data 
        # a single space used as the separator between values when printing.
        # comma prevents newline character from being printed so subsequent prints continue on same line.
        print(root.value, end=" "), 
        # Recur on right
        traverseInorder(root.right)


# Preorder Algorithm
# 1. Visit root
# 2. Traveres L subtree
# 3. Traverse R subtree

def traversePreorder(root):
    """
    Time Complexity: O(N)
    Space: without size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree. 
    """
    if root:
        # Print data of node
        print(root.value, end=" "),
        # Recur L child
        traversePreorder(root.left)
        # Recur R child
        traversePreorder(root.right)


# Postorder Algorithm
# 1. Traverse L subtree
# 2. Traverse R subtree
# 3. Visit root

def traversePostorder(root):
    """
    """
    if root:
        traversePostorder(root.left)
        traversePostorder(root.right)
        print(root.value, end=" "),
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

"""
      1
    /   \
   2     3
  / \
 4   5
"""

print("Inorder traversal of binary tree: ")
traverseInorder(root)

# Preorder traversal is used to create a copy of the tree
print("\nPreorder traversal of binary tree: ")
traversePreorder(root)

# Postorder traversal is used to delete the tree
print("\nPostorder traversal of binary tree: ")
traversePostorder(root)