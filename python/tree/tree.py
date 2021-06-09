# from collections import deque
class QueueNode:
  def __init__(self, value, next_=None):
    self.value = value
    self.next = next_
  
class Queue:
  """This class is a queue
  """
  def __init__(self, front=None):
    self.front = front
    self.back = None
    
  def enqueue(self, value=None):
    if self.front is None:
      self.front = self.back = QueueNode(value)
    else:
      self.back.next = QueueNode(value)
    
  def dequeue(self):
    if self.front is None:
      return 
    ret = self.front.value
    self.front = self.front.next
    return ret
    
  def peek(self):
    if self.front is not None:
      return self.front.value
    return 
  
  
  

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
    
class BinaryTree:
  def __init__(self):
    self.root = None
    
  @staticmethod
  def breadth_first(tree):
    collection = []
    queue = Queue()
    queue.enqueue(tree.root)
    
    while queue.peek():
      node = queue.dequeue()
      collection.append(node.value)
      if node.left:
        queue.enqueue(node.left)
      if node.right:
        queue.enqueue(node.right)
    
    return collection
      
  # @staticmethod  
  # def breadth_first(tree=None):
  #   collection = []
  #   queue = Queue()
  #   queue.append(tree.root)
    
  #   if not tree:
  #     return []
      
    
  #   while (len(queue) >0) and not ValueError:
  #     collection.append(queue[0].value)
  #     if queue[0].left:
  #       queue.enqueue(queue[0].left)
  #     if queue[0].right:
  #       queue.enqueue(queue[0].right)
        
  #     queue.dequeue()
      
  #   return collection
    
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
      
      
    
  
    