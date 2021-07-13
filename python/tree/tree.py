class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    
class BinaryTree:
  def __init__(self):
    self.root = None
    
  def add(self, value):
    if not self.root:
      self.root = Node(value)
      return
    
    def walk(root):
      if not root:
        return
      
      if not root.left:
        root.left = Node(value)
        return
      if root.left and not root.right:
        root.right = Node(value)
        return
      walk(root.left)
      walk(root.right)
        
    walk(self.root)
    
  def max_value(self):
    counter = 0
    
    if not self.root:
      return
    
    def walk(root):
      nonlocal counter
      if not root:
        return
      
      if root.value > counter:
        counter = root.value
      walk(root.left)
      walk(root.right)
      
    walk(self.root)
    
    return counter
        
    
class BinarySearchTree(BinaryTree):
  def add(self, value):
    if not self.root:
      self.root = Node(value)
      return
    
    def walk(root):
      if not root:
        return 
      
      if value < root.value:
        if root.left:
          walk(root.left)
        if not root.left:
          root.left = Node(value)
          
      if value > root.value:
        if root.right:
          walk(root.right)
        if not root.right:
          root.right = Node(value)
          
    walk(self.root)
    
    
  
    
  def contains(self, value):
    if self.root.value == value:
      return True
    
    def walk(root, value):
      if not root:
        return False
      if root.value == value:
        return True
      
      if value < root.value:
        return walk(root.left, value)
      if value > root.value:
        return walk(root.right, value)
      
        
    return walk(self.root, value)
  
  def pre_order_traversal(self, do_thing=print):
    collection = []
    
    if not self.root:
      return collection
    
    def walk(root, collection):
      if (not root) and collection:
        return collection
      
      collection.append(root.value)
      walk(root.left, collection)
      walk(root.right, collection)
    walk(self.root, collection)

    if do_thing == print:
      [print(i) for i in collection]
      
    return collection
  
  def in_order_traversal(self):
    collection = []
    
    if not self.root:
      return collection
    
    def walk(root, collection):
      if not root:
        return collection
      walk(root.left, collection)
      collection.append(root.value)
      walk(root.right, collection)
    walk(self.root, collection)
      
    return collection
  
  def post_order_traversal(self):
    collection = []
    
    if not self.root:
      return collection
    
    def walk(root, collection):
      if not root:
        return collection
      walk(root.left, collection)
      walk(root.right, collection)
      collection.append(root.value)
    walk(self.root, collection)
      
    return collection
      
      
    
  
    