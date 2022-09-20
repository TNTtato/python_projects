from random import sample

def merge_sort(args):
  if len(args) <= 1:
    return args
  
  mid = len(args) // 2
  left_half = merge_sort(args[0:mid])
  right_half = merge_sort(args[mid:])
  
  li = []
  while left_half and right_half:
    if left_half[0] < right_half[0]:
      li.append(left_half.pop(0)) 
    else:
      li.append(right_half.pop(0))

  return li + left_half + right_half 

unorder_list = sample(range(1, 100 + 1), 10)

print(merge_sort(unorder_list))