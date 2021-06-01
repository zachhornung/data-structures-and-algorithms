class Node:
  def __init__(self, value, next_=None):
    self.value = value
    self.next = next_
    
  
class Stack:
  def __init__(self, top=None):
    self.top = top
    
  def push(self, value):
    self.top = Node(value, self.top)
    
  def pop(self):
    if self.top:
      ret = self.top.value
      self.top = self.top.next
      return ret
    return 'this stack is empty buddy'
  
  def peek(self):
    if self.top:
      return self.top.value
    return 'this stack is empty buddy'
  
  def isempty(self):
    return self.top is None
  

class Queue:
  """This class is a queue
  """
  def __init__(self, front=None):
    self.front = front
    self.back = None
    
  def enqueue(self, value=None):
    if self.front is None:
      self.front = self.back = Node(value)
    else:
      self.back.next = Node(value)
    
  def dequeue(self):
    if self.front is None:
      return 'this queue is empty buddy'
    ret = self.front.value
    self.front = self.front.next
    return ret
    
  def peek(self):
    if self.front is not None:
      return self.front.value
    return 'this queue is empty buddy'
      