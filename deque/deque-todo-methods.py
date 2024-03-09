class Deque:
  def __init__(self):
    self.elements = []
  def add_first(item):
    # Implement in "Implementing add_first()"
    pass
  def add_last(item):
    # Implement in "Implementing add_last()"
    pass
  def remove_first():
    # Implement in "Implementing remove_first()"
    pass
  def remove_last():
    # Implement in "Implementing remove_last()"
    pass
  def is_empty():
    # Implement in "Implementing is_empty() and size()"
    pass
  def size():
     # Implement in "Implementing is_empty() and size()"
    pass
  def peek_first(self):
    return self.elements[-1]
  def peek_last(self):
    return self.elements[0]
  def display_deque(self):
    print('\t | \t'.join(str(item) for item in self.elements))
