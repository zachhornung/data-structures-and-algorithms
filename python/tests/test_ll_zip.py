import pytest
from ll_zip.ll_zip import zip_lists
from linked_list.linked_list import LinkedList, Node

ll1 = LinkedList()
ll1.insert('babies')
ll1.insert('goats')
ll1.insert('chickens')
ll1.insert('farm animals')
ll1.insert('roosters')

ll2 = LinkedList()
ll2.insert('potatos')
ll2.insert('peppers')
ll2.insert('peas')
ll2.insert('cucumbers')
ll2.insert('veggies')

def test_zip_lists_import():
  assert zip_lists(ll1, ll2) == 'babies'

def test_zip_lists():
  assert ll1.head.next.value == 'veggies'

def test_zip_lists_in_place():
  assert str(ll1) == 'roosters --> veggies --> farm animals --> cucumbers --> chickens --> peas --> goats --> peppers --> babies --> potatos --> None'