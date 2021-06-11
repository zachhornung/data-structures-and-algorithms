from collections import deque

def fizz_buzz_tree(tree):
  return tree.clone(fizzify)

def fizzy_copy(node):
  fizzy_value = fizzify(node.value)
  return Node(fizzy_value)

def fizzify(value):
  fizzy_value = ''
  if value % 3 == 0:
    fizzy_value += 'Fizz'
    
  if value % 5 == 0:
    fizzy_value += 'Buzz'
    
  return fizzy_value or str(value)

class Queue:
  def __init__(self):
    self.storage = deque()
    
  def enqueue(self, value):
    self.storage.append(value)
    
  def dequeue(self):
    if self.is_empty():
      raise EmptyError(self.dequeue)
    
    return self.storage.popleft()
  
  def peek(self):
    if self.is_empty():
      raise EmptyError(self.peek)
    
    return self.storage[0]
  
  def is_empty(self):
    return len(self.storage) == 0
  
  
class EmptyError(Exception):
  def __init__(self, method):
    super().__init__(f'cannot call {method.__name__} method on empty Queue')


class Node:
  def __init__(self, value):
    self.value = value
    self.children = []
    
  def clone(self, converter=None):
    value = self.value
    if converter:
      value = converter(value)
      
    return Node(value)
  
class KaryTree:
  def __init__(self, root=None):
    self.root = root
    
  def breadth_first(self):
    queue = Queue()
    
    collection = []
    
    queue.enqueue(self.root)
    
    while not queue.is_empty():
      node = queue.dequeue()
      collection.append(node.value)
      for child in node.children:
        queue.enqueue(child)
        
    return collection
  
  def clone(self, converter=None):
    
    clone_root = self.root.clone(converter)
    clone_tree = KaryTree(clone_root)
    
    pairs = Queue()
    pairs.enqueue((self.root, clone_root))
    
    while not pairs.is_empty():
      source_node, clone_node = pairs.dequeue()
      for source_child_node in source_node.children:
        clone_child_node = source_child_node.clone(converter)
        pair = (source_child_node, clone_child_node)
        pairs.enqueue(pair)
        clone_node.children.append(clone_child_node)
        
    return clone_tree