# from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree, KAry_tree, KNode

# def test_import():
#   assert fizz_buzz_tree

# def test_KAry_tree_and_KNode_import():
#   assert KAry_tree and KNode

# def test_KAry_tree_add_initial_value():
#   k_tree = KAry_tree(4)
#   k_tree.add(node=KNode('babies', {'chickens': None}))
#   assert k_tree.root.value == 'babies' and k_tree.root.children['chickens'] == None
  
# def test_fizz_buzz_tree():
#   k_tree = KAry_tree(4)
#   five = KNode(5)
#   six = KNode(6)
#   fifteen = KNode(15)
#   eight = KNode(8)
#   three = KNode(3)
  
#   five.children[6] = six
#   five.children[8] = eight
#   five.children[3] = three
#   six.children[15] = fifteen
#   k_tree.add(node=five)
#   clone_tree = k_tree.copy()
#   assert k_tree.root.children[6].children[15].value == k_tree.root.children[6].children[15].value
  
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

from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree, Node, KaryTree


def test_one_to_15():

    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    """
                            1
                2                       3
            4  5  6               7     8          9
        10  11 12              13            14   15
    """

    one.children = [two, three]
    two.children = [four, five, six]
    three.children = [seven, eight, nine]
    four.children = [ten]
    five.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    nine.children = [fourteen, fifteen]

    kt = KaryTree()
    kt.root = one

    fizzy_tree = fizz_buzz_tree(kt)

    actual = fizzy_tree.breadth_first()
    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]

    assert actual == expected

    assert kt.breadth_first() == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    ]


def test_not_same_tree():

    tree = KaryTree(Node(1))

    clone = tree.clone()

    tree.root.value = 0

    assert tree.root.value == 0
    assert clone.root.value == 1