def insertion_sort(arr):
  for index, value in enumerate(arr):
    j = index-1
    while j >= 0 and value < arr[j]:
      arr[j+1] = arr[j]
      j-=1
    arr[j+1] = value