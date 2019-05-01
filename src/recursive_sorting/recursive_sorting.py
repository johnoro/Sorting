from random import randint
def quick_sort(arr):
  pivot = randint(0, len(arr) - 1)
  left = []
  right = []
  for num in arr[:pivot] + arr[pivot+1:]:
    if num < arr[pivot]:
      left.append(num)
    else:
      right.append(num)
  if len(left) > 1:
    left = quick_sort(left)
  if len(right) > 1:
    right = quick_sort(right)
  return left + [arr[pivot]] + right


print(quick_sort([1, 3, 6, 2, 13, 41, 7]))

from collections import deque
def merge(arrA, arrB):
  queueA = deque(arrA)
  queueB = deque(arrB)
  merged = []

  while len(queueA) > 0 and len(queueB) > 0:
    if queueB[0] < queueA[0]:
      merged.append(queueB.popleft())
    else:
      merged.append(queueA.popleft())
  
  merged.extend(queueA)
  merged.extend(queueB)

  return merged

def merge_sort(arr):
  if len(arr) < 2:
    return arr

  mid = len(arr) // 2

  return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


print(merge_sort([1, 3, 6, 2, 13, 41, 7]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
  queueA = deque(arr[start:mid])
  queueB = deque(arr[mid:end])
  i = start

  while len(queueA) > 0 and len(queueB) > 0:
    if queueB[0] < queueA[0]:
      arr[i] = queueB.popleft()
    else:
      arr[i] = queueA.popleft()
    i += 1

  while len(queueA) > 0:
    arr[i] = queueA.popleft()
    i += 1
  while len(queueB) > 0:
    arr[i] = queueB.popleft()
    i += 1

  return arr

def merge_sort_in_place(arr,l=0,r=0):
  def sort(left, right):
    if right-left > 1:
      mid = (left+right) // 2
      sort(left, mid)
      sort(mid, right)
      merge_in_place(arr, left, mid, right)
    return arr
  return sort(0, len(arr))

print(merge_sort([1, 3, 6, 2, 13, 41, 7]))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
  return arr
