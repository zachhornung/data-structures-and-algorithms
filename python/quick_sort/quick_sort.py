# quick_sort order of leaving the stack
#[0,-1] quick_sort(lst, left, position - 1)
#[1,1] quick_sort(lst, position +1, right)
#[0,1] quick_sort(lst, left, position - 1)
#[3,3] quick_sort(lst, left, right)
#[5,5] quick_sort(lst, position +1, right)
#[3,5] quick_sort(lst, position +1, right)
#[0,5] quick_sort(lst, left, right)
#
#
#
stack_height = 0
def quick_sort(lst, left, right):
    global stack_height
    stack_height +=1
    # print('left and right coming in: ',left,right,'stack height: ',stack_height)
    if left < right:
      # print('sorting')
      position = partition(lst, left, right)
      quick_sort(lst, left, position - 1)
      # print('done with left')
      quick_sort(lst, position +1, right)
      # print('done with right and out of the sort')

    stack_height -= 1
    # print('coming off the stack: ', left, right, 'stack height: ',stack_height)
    
    return lst


def partition(lst, left, right):
  pivot = lst[right]
  low = left -1
  for i in range(left, right):
    if lst[i] <= pivot:
      low += 1
      # print('swapping: ',lst, lst[i], lst[low])
      swap(lst, i, low)
  # print('swapping: ',lst, lst[right],lst[low+1])
  swap(lst, right, low +1)
  
  return low + 1
  


def swap(lst, i, low):
  temp = lst[i]
  lst[i] = lst[low] 
  lst[low] = temp
  
# Sample Lists
# [8,4,23,42,16,15]
# [2,3,5,7,13,11]
# [5,12,7,5,5,7]
# [20,18,12,8,5,-2]