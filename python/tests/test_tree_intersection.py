from tree_intersection.tree_intersection import find_common_values
from tree.tree import Node, BinaryTree, BinarySearchTree

def test_imports():
  assert find_common_values and Node and BinaryTree and BinarySearchTree
  
def test_find_common_values():
  tree1 = BinarySearchTree()
  tree2 = BinarySearchTree()
  tree1.add(11)
  tree1.add(22)
  tree1.add(33)
  tree1.add(66)
  tree1.add(55)
  tree1.add(44)
  tree1.add(12)
  tree1.add(32)
  tree1.add(34)
  tree1.add(43)
  
  tree2.add(111)
  tree2.add(22)
  tree2.add(331)
  tree2.add(66)
  tree2.add(551)
  tree2.add(44)
  tree2.add(121)
  tree2.add(32)
  tree2.add(341)
  tree2.add(43)
  
  common_values = find_common_values(tree1, tree2)
  assert common_values == [22, 32, 66, 44, 43]
  
def test_this_should_be_false():
  tree1 = BinarySearchTree()
  tree2 = BinarySearchTree()
  tree1.add(11)
  tree1.add(22)
  tree1.add(33)
  tree1.add(66)
  tree1.add(55)
  tree1.add(44)
  tree1.add(12)
  tree1.add(32)
  tree1.add(34)
  tree1.add(43)
  
  tree2.add(111)
  tree2.add(22)
  tree2.add(331)
  tree2.add(66)
  tree2.add(551)
  tree2.add(44)
  tree2.add(121)
  tree2.add(32)
  tree2.add(341)
  tree2.add(43)
  
  common_values = find_common_values(tree1, tree2)
  assert common_values != [22, 32, 66, 44, 43,1,1,1,1,1,2,2,2,2,3,3,3,3,3] and common_values != []
  
def test_empty_return():
  tree1 = BinarySearchTree()
  tree2 = BinarySearchTree()
  common_values = find_common_values(tree1, tree2)
  assert common_values == []
  

