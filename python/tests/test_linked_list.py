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



