from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree, KAry_tree, KNode

def test_import():
  assert fizz_buzz_tree

def test_KAry_tree_and_KNode_import():
  assert KAry_tree and KNode

def test_KAry_tree_add_initial_value():
  k_tree = KAry_tree(4)
  k_tree.add(node=KNode('babies', {'chickens': None}))
  assert k_tree.root.value == 'babies' and k_tree.root.children['chickens'] == None
  
def test_fizz_buzz_tree():
  k_tree = KAry_tree(4)
  five = KNode(5)
  six = KNode(6)
  fifteen = KNode(15)
  eight = KNode(8)
  three = KNode(3)
  
  five.children[6] = six
  five.children[8] = eight
  five.children[3] = three
  six.children[15] = fifteen
  k_tree.add(node=five)
  clone_tree = k_tree.copy()
  assert k_tree.root.children[6].children[15].value == k_tree.root.children[6].children[15].value
  
# def test_buzzy_children():
#   k_tree = KAry_tree(3)
#   node = KNode('5', {'6': None})
#   k_tree.add(node=node)
#   another_node = KNode('6', {'15': None})
#   k_tree.add(node=another_node)
#   k_tree.add(value='15')
#   k_tree.add(value='8')
#   k_tree.add(value='3')
#   fizzbuzz_tree = fizz_buzz_tree(k_tree)
#   assert 'fizz' == fizzbuzz_tree.root.children['6'].value