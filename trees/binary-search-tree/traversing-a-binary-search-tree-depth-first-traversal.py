class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None

  def insert(self, value):
    if (value < self.value):
      if (self.left is None):
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)
    else:
      if (self.right is None):
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)
        
  def get_node_by_value(self, value):
    if (self.value == value):
      return self
    elif ((self.left is not None) and (value < self.value)):
      return self.left.get_node_by_value(value)
    elif ((self.right is not None) and (value >= self.value)):
      return self.right.get_node_by_value(value)
    else:
      return None
    
  # Define .depth_first_traversal() below:
  def depth_first_traversal(self):
    if self.left is not None:      
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if self.right is not None:      
      self.right.depth_first_traversal()
    
tree = BinarySearchTree(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)

# Print depth-first traversal:
tree.depth_first_traversal()

"""
Tree node 24 added to the left of 48 at depth 2
Tree node 55 added to the right of 48 at depth 2
Tree node 26 added to the right of 24 at depth 3
Tree node 38 added to the right of 26 at depth 4
Tree node 56 added to the right of 55 at depth 3
Tree node 74 added to the right of 56 at depth 4
Depth=2, Value=24
Depth=3, Value=26
Depth=4, Value=38
Depth=1, Value=48
Depth=2, Value=55
Depth=3, Value=56
Depth=4, Value=74
"""

"""
   48
  /  \
24    55
  \     \
   26    56
     \     \
      38    74
"""

