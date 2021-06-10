from stacks_and_queues.stacks_and_queues import Queue, Node

class KNode:
  def __init__(self, value=None, children={}):
    self.value = value
    self.children = children

class KAry_tree:
  def __init__(self, root=None):
    self.root = root
    
  def add(self, value, node=None):
    node_to_add = KNode(value)
    
    if node:
      node_to_add == node
      value = node.value
      
    if not self.root:
      self.root = node_to_add
      return
      
    if not self.root.children:
      self.root.children[value] = node_to_add
      return
    
    current = self.root
    running = True
    while running:
      if (value in current.children) and (current.children[value] == None):
        current.children[value] == node_to_add
        running = False
        continue
      #check to see if the value points to a node that is supossed to have that value as a child. if it does, go to that node.
      if (value in current.children) and (current.children[value] != None):
        current = current.children[value]
        value = current.children[value].value
      else:
        
      # if it doesnt, then set a child node for the current value to be 
        print('im looping')
        current.children[value] = node_to_add
        running = False
    
      

def fizz_buzz_tree(tree=None):
  if not tree.root:
    return
  
  queue = Queue()
  new_fizzbuzz_tree = KAry_tree()
  queue.enqueue(tree.root)
  
  while queue.peek():
    current = queue.dequeue()
    if current.children:
      for child in current.children:
        queue.enqueue(current.children[child])
      
    old_value = current.value
    
    if int(current.value) % 15 == 0:
      current.value == 'fizzbuzz'
    elif int(current.value) % 5 == 0:
        current.value = 'buzz'
    elif int(current.value) % 3 == 0:
      current.value = 'fizz'

    current.value = str(current.value)
    new_fizzbuzz_tree.add(old_value, current)
    
  return new_fizzbuzz_tree
    
    