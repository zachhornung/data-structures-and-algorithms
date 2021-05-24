from linked_list.linked_list import LinkedList, Node
import pytest


def test_import():
    assert LinkedList


def test_linked_list_exits():
    lst = LinkedList()
    assert lst

def test_insert_node():
    lst = LinkedList()
    lst.insert('baby goats')
    assert lst.head.value == 'baby goats'

def test_insert_multiple_things():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    assert lst.head.next.value == 'baby goats'

def test_includes_method():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    assert lst.includes('baby goats')

def test_to_string_method():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    assert str(lst) == 'more goats --> baby goats --> None'

def test_append():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    lst.append('water')
    assert str(lst) == 'more goats --> baby goats --> water --> None'

def test_insert_before():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    lst.append('water')
    lst.insert_before('baby goats', 'before')
    assert str(lst) == 'more goats --> before --> baby goats --> water --> None'

def test_insert_after():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    lst.append('water')
    lst.insert_before('baby goats', 'before')
    lst.insert_after('baby goats', 'after')
    assert str(lst) == 'more goats --> before --> baby goats --> after --> water --> None'

def test_insert_before_first_node():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    lst.append('water')
    lst.insert_before('baby goats', 'before')
    lst.insert_after('baby goats', 'after')
    lst.insert_before('more goats', 'it worked!')
    assert str(lst) == 'it worked! --> more goats --> before --> baby goats --> after --> water --> None'

def test_insert_after_last_node():
    lst = LinkedList()
    lst.insert('baby goats')
    lst.insert('more goats')
    lst.append('water')
    lst.insert_before('baby goats', 'before')
    lst.insert_after('baby goats', 'after')
    lst.insert_before('more goats', 'it worked!')
    lst.insert_after('water', 'drought')
    assert str(lst) == 'it worked! --> more goats --> before --> baby goats --> after --> water --> drought --> None'



