class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

# Create a new BST:
root = BinarySearchTree(15)
# Print root's value below:
print(root.value)
