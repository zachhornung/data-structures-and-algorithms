def find_common_values(tree1, tree2):
  return [item for item in tree1.pre_order_traversal() if item in tree2.pre_order_traversal()]