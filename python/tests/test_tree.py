from tree.tree import Node, BinaryTree, BinarySearchTree

def test_imports():
  assert Node and BinaryTree and BinarySearchTree
  
def test_binary_search_tree_has_root():
  tree = BinarySearchTree()
  assert tree.root == None
  
def test_root_has_left():
  tree = BinarySearchTree()
  tree.add(5)
  assert tree.root.left == None
  
def test_root_has_right():
  tree = BinarySearchTree()
  tree.add(5)
  assert tree.root.right == None
  
def test_add_multiple_small_values():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(4)
  tree.add(3)
  tree.add(2)
  assert tree.root.left.left.left.value == 2
  
def test_add_multiple_right():
  tree = BinarySearchTree()
  tree.add(2)
  tree.add(3)
  tree.add(4)
  tree.add(5)
  assert tree.root.right.right.right.value == 5
  
def test_contains():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(6)
  tree.add(4)
  tree.add(3)
  assert tree.contains(5) == True
  
def test_contains_but_value_isnt_there():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(6)
  tree.add(4)
  tree.add(3)
  assert tree.contains(99) == False
  
def test_pre_order_traversal():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(6)
  tree.add(4)
  tree.add(3)
  assert tree.pre_order_traversal() == [5,4,3,6]
  
def test_in_order_traversal():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(6)
  tree.add(4)
  tree.add(3)
  assert tree.in_order_traversal() == [3,4,5,6]
  
def test_post_order_traversal():
  tree = BinarySearchTree()
  tree.add(5)
  tree.add(6)
  tree.add(4)
  tree.add(3)
  
  """
          5
        4    6
      3  
  """ 
  assert tree.post_order_traversal() == [3,4,6,5]
  
def test_add_regular_binary_tree():
  reg_tree = BinaryTree()
  reg_tree.add(1)
  reg_tree.add(2)
  reg_tree.add(5)
  reg_tree.add(3)
  reg_tree.add(6)
  assert (reg_tree.root.value == 1) and (reg_tree.root.left.value == 2) and (reg_tree.root.right.value == 5) and (reg_tree.root.left.right.value == 6)
  
def test_find_max_value():
  reg_tree = BinaryTree()
  reg_tree.add(1)
  reg_tree.add(2)
  reg_tree.add(5)
  reg_tree.add(3)
  reg_tree.add(6)
  assert reg_tree.max_value() == 6
  
def test_breadth_first():
  reg_tree = BinaryTree()
  reg_tree.add(1)
  reg_tree.add(2)
  reg_tree.add(5)
  reg_tree.add(3)
  reg_tree.add(6)
  assert BinaryTree.breadth_first(reg_tree) == [1,2,5,3,6]