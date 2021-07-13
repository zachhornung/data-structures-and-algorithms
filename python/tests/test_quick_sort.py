from quick_sort.quick_sort import quick_sort, partition, swap
import random

def test_imports():
  assert quick_sort and partition and swap
  
def test_quick_sort():
  array = [12,89,23,78,34,78,45,67]
  quick_sort(array,0,7)
  assert array == [12,23,34,45,67,78,78,89]
  
def test_big_array_sort():
  array = [1,2,3,4,5,4,2,4,4,3,6,5,6,3,5,6,4,6,5,2435,543,234,654,567,76,789,987,345,432,123,345,456,567,678,686,543545,35454,354576767,464543423,4556677889,434354656778,775645434233454657,7879755,34232,4354657,676878,7978,664,53434,34]
  copy_array = array
  copy_array.sort()
  quick_sort(array,0,len(array)-1)
  assert array == copy_array
  
def test_big_boi():
  array = [random.randrange(0,5000,1) for _ in range(500)]
  copy_array = array
  copy_array.sort()
  quick_sort(array,0,len(array)-1)
  assert array == copy_array
  