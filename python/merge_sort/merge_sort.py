def merge_sort(arr):
  n = len(arr)
  
  if n > 1:
    mid = n//2
    left = arr[:mid]
    print('left: ',left)
    right = arr[mid:]
    print('right: ', right)
    merge_sort(left)
    merge_sort(right)
    print('merging: ', left, right, 'passed arr: ', arr)
    merge(left, right, arr)
    print('arr after merge: ',arr)

def merge(left, right, arr):
  i=j=k=0

  while (i < len(left)) and (j < len(right)):
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
      k += 1
      continue
    
    arr[k] = right[j]
    j += 1
    k += 1

  while i < len(left):
    arr[k] = left[i]
    k += 1
    i += 1

  while j < len(right):
    arr[k] = right[j]
    k += 1
    j += 1