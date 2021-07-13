from insertion_sort.insertion_sort import insertion_sort

def test_import():
  assert insertion_sort
  
def test_sort_works():
  arr = [6,5,4,3,2,1]
  insertion_sort(arr)
  assert arr == [1,2,3,4,5,6]