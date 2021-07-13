from merge_sort.merge_sort import merge_sort

def test_import():
  assert merge_sort
  
def test_that_it_really_does_sort():
  arr = [9,8,7,6,5,4,3,2,1]
  merge_sort(arr)
  assert arr == [1,2,3,4,5,6,7,8,9]
  
def test_this_is_not_supossed_to_happen():
  arr = [9,8,7,6,5,4,3,2,1]
  merge_sort(arr)
  assert arr != [1,2,3,4,6,7,8,9,5]