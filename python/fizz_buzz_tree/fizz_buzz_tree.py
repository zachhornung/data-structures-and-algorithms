from stacks_and_queues.stacks_and_queues import Queue, Node

class KNode:
  def __init__(self, value=None, children={}, previous_value=None):
    self.previous_value = previous_value
    self.value = value
    self.children = children

class KAry_tree:
  def __init__(self, k=5, root=None):
    self.k = k
    self.root = root
    self.map = {}
    
    
        
  # def walk(node, node_to_add):
  #   if not node.children:
  #     return
  #   for index in node.children:
  #     if node.children[index] == None
  #   child_number = len(node.children)
  #   walk(node.children[child_number+1], node_to_add)
      
    
  def add(self, **kwargs):
    if 'value' in kwargs:
      node_to_add = KNode(kwargs['value'])
      value = kwargs['value']
    if 'node' in kwargs and not 'value' in kwargs:
      node_to_add = kwargs['node']
      value = node_to_add.value
      
    if not self.root:
      self.root = node_to_add
      return
      
    if not self.root.children:
      self.root.children[value] = node_to_add
      return
    
    current = self.root
    while True:
      # if this is where the node is supossed to be, then put it here and break the loop.
      if (value in current.children) and (current.children[value] == None):
        current.children[value] == node_to_add
        break
      #check to see if the value points to a node that is supossed to have that value as a child. if it does, go to that node.
      if (value in current.children) and (current.children[value] != None):
        # i think i need recursive walk call here to check out all of the children in the current and next nodes to see if the 
        # current node is suppossed to go further down the tree
        current = current.children[value]
        value = current.children[value].value
        continue
      # if it doesnt, then set a child node for the current value to be 
      print('looping')
      current.children[value] = node_to_add
      break
  
  def copy(self):
    if not self.root:
      return
      # make a copy of the tree and just put the root and its children in there as a new node
    clone_root = KNode(self.root.value)
    copy_tree = KAry_tree()
    copy_tree.root = clone_root

    queue = Queue()
    queue.enqueue((self.root, clone_root))

    while queue.peek():
      og_node, copy_node = queue.dequeue()
    
      if og_node.children:
        for child in og_node.children:
          copy_child = KNode(og_node.children[child].value)
          queue.enqueue((og_node.children[child], copy_child))
          copy_node.children[child] = copy_child
    
    return copy_tree

def fizz_buzz_tree(tree_og=None):
  if not tree_og or not tree_og.root:
    return
  # make a copy of the tree and just put the root and its children in there as a new node
  copy_tree = KAry_tree()
  copy_tree.root = KNode(tree_og.root.value)
  
  queue = Queue()
  queue.enqueue((tree_og.root, copy_tree.root))
  
  while queue.peek():
    og_node, copy_node = queue.dequeue()
    
    if og_node.children:
      for child in og_node.children:
        copy_child = KNode(og_node.children[child].value)
        queue.enqueue((og_node.children[child], copy_child))
        copy_node.children[child] = copy_child
        
    
    # keys = og_node.children.keys()
    # for key in keys:
    #   if int(key) % 3 == 0:
    #     copy_node.children['fizz'] = current.children.pop(key)
    #   if int(key) % 5 == 0:
    #     current.children['buzz'] = current.children.pop(key)
    #   if int(key) % 15 == 0:
    #     current.children['fizzbuzz'] = current.children.pop(key)
    # i think i also need to change the key values for a child if the key value will be changed to fizz, buzz or fizzbuzz
    # so that when i add it to the new kary tree it will know where it goes and where its kids go
    
    
    
    if current.value % 3 == 0:
      current.value = 'fizz'
    
    if current.value % 5 == 0:
        current.value = 'buzz'
      
    if current.value % 15 == 0:
      current.value == 'fizzbuzz'

    new_fizzbuzz_tree.add(node=current)
    
  return new_fizzbuzz_tree
    
    