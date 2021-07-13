from left_join_hash_maps.left_join_hash_maps import left_join
import string

def test_imports():
  assert left_join
  
def test_left_join():
  d1 = {char:char for char in string.ascii_lowercase}
  d2 = {char:(char+char if i%2 ==0 else char) for i,char in enumerate(string.ascii_lowercase)}
  assert left_join(d1, d2) == [['a', 'a', 'aa'], ['b', 'b', 'b'], ['c', 'c', 'cc'], ['d', 'd', 'd'], ['e', 'e', 'ee'], ['f', 'f', 'f'], ['g', 'g', 'gg'], ['h', 'h', 'h'], ['i', 'i', 'ii'], ['j', 'j', 'j'], ['k', 'k', 'kk'], ['l', 'l', 'l'], ['m', 'm', 'mm'], ['n', 'n', 'n'], ['o', 'o', 'oo'], ['p', 'p', 'p'], ['q', 'q', 'qq'], ['r', 'r', 'r'], ['s', 's', 'ss'], ['t', 't', 't'], ['u', 'u', 'uu'], ['v', 'v', 'v'], ['w', 'w', 'ww'], ['x', 'x', 'x'], ['y', 'y', 'yy'], ['z', 'z', 'z']]
  
def test_right_join():
  d1 = {char:char for char in string.ascii_lowercase}
  d2 = {char:(char+char if i%2 ==0 else char) for i,char in enumerate(string.ascii_lowercase)}
  assert left_join(d1, d2, right_join=True) == [['a', 'aa', 'a'], ['b', 'b', 'b'], ['c', 'cc', 'c'], ['d', 'd', 'd'], ['e', 'ee', 'e'], ['f', 'f', 'f'], ['g', 'gg', 'g'], ['h', 'h', 'h'], ['i', 'ii', 'i'], ['j', 'j', 'j'], ['k', 'kk', 'k'], ['l', 'l', 'l'], ['m', 'mm', 'm'], ['n', 'n', 'n'], ['o', 'oo', 'o'], ['p', 'p', 'p'], ['q', 'qq', 'q'], ['r', 'r', 'r'], ['s', 'ss', 's'], ['t', 't', 't'], ['u', 'uu', 'u'], ['v', 'v', 'v'], ['w', 'ww', 'w'], ['x', 'x', 'x'], ['y', 'yy', 'y'], ['z', 'z', 'z']]
  
def test_right_join_different_number_of_elements_in_each_dict():
  d1 = {char:char for char in string.ascii_lowercase}
  d2 = {char:(char+char if i%2 ==0 else char) for i,char in enumerate(string.ascii_lowercase[:13])}
  assert left_join(d1,d2, right_join=True) == [['a', 'aa', 'a'], ['b', 'b', 'b'], ['c', 'cc', 'c'], ['d', 'd', 'd'], ['e', 'ee', 'e'], ['f', 'f', 'f'], ['g', 'gg', 'g'], ['h', 'h', 'h'], ['i', 'ii', 'i'], ['j', 'j', 'j'], ['k', 'kk', 'k'], ['l', 'l', 'l'], ['m', 'mm', 'm']]
  
def test_this_shouldnt_happen():
  d1 = {char:char for char in string.ascii_lowercase}
  d2 = {char:(char+char if i%2 ==0 else char) for i,char in enumerate(string.ascii_lowercase)}
  assert (left_join(d1,d2) != ['babies','goats','baby goats']) and (left_join(d1,d2) != [])